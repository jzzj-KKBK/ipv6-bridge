import socket
import select
import threading
import json
import os

def handle_client(client_socket):
    print("正在连接")
    try:
        # 连接到目标服务器
        with socket.create_connection((TARGET_HOST, TARGET_PORT)) as target_socket:
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
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as server_socket:
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

#这里是服务器 客户端应该与他相反
if __name__ == "__main__":
    try:
        with open('conf.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            IP = '::'                                       # IPv6转发
            port = int(data['server_port'])                 # 转发端口
            TARGET_HOST = '127.0.0.1'                       # 本地换回接口
            TARGET_PORT = int(data['game_port'])                             # 假设 Minecraft 服务器运行在这个端口
    except:
        print("出错！需要修改配置")
        print("是否要启动半自动模式？(Y/N)")
        yn=input("")
        if yn == "Y":
            os.system("chcp 65001&&ipconfig")
            print("请输入你的公网IPv6")
            server_IPv6=input("")
            os.system("chcp 65001&&netstat -ano | findstr LISTENING | findstr 0.0.0.0:")
            print("请输入你游戏的端口")
            server_port=input("")
        else:
            print("请自行输入")
            server_IPv6=''
            server_port=''
        config = {
            "user_local_IP":"127.0.0.1",                                         # 客户端的换回接口(你爱连啥都可以)
            "user_local_port":"46666",                                           # 客户端的转发端口(你进游戏要用的)
            "server_IPv6":""+server_IPv6,                                                    # 服务器的IP
            "server_port":""+server_port,                                                    # 服务器的转发端口
            "game_port":"64871"}                                                 # 游戏的端口
        with open('conf.json', 'w') as f:
            json.dump(config, f, indent=4)
        print("重启进程即可")
    TCPlink()

