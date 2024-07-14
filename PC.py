import socket
import select
import threading


def handle_client(client_socket):
    print("正在连接")
    try:
        # 连接到目标服务器
        with socket.create_connection((TARGET_HOST, TARGET_PORT)) as target_socket:
            message = f"{IP}:{port}".encode('utf-8')
            client_socket.sendall(message)
            # 使用 select 来监听两个 socket 的可读性
            inputs = [client_socket, target_socket]
            while inputs:
                readable, _, _ = select.select(inputs, [], [])
                for s in readable:
                    data = s.recv(4096)
                    if s is client_socket:
                        # 从客户端接收数据，并发送到目标服务器
                        if data:
                            target_socket.sendall(data)
                        else:
                            # 客户端关闭了连接
                            inputs.remove(s)
                            target_socket.close()
                            break
                    else:
                        # 从目标服务器接收数据，并发送到客户端
                        if data:
                            client_socket.sendall(data)
                        else:
                            # 目标服务器关闭了连接
                            inputs.remove(s)
                            client_socket.close()
                            break
    finally:
        client_socket.close()


def TCPlink():
    # 创建一个 TCP 套接字并绑定到代理服务器的地址和端口
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((IP, port))
        server_socket.listen(5)
        print(f"Proxy listening on {IP}:{port}")
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            # 为每个客户端连接创建一个新线程
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
#客户端的配置应该与服务器相反
if __name__ == "__main__":
    IP = '127.0.0.1'
    port = 46666
    TARGET_HOST = '::'
    TARGET_PORT = 43325  # 服务器的转发
    TCPlink()