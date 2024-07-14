# IPv6桥

#### 介绍
老旧的游戏无法支持IPv6，仅支持IPv4。但是IPv4地址枯竭，所以想到用Python转发游戏TCP流量
nginx虽然高性能，但是配置麻烦
没有公网IP地址使得很多老游戏根本没办法进行联机，但是又不想买 腾讯云/阿里云/华为云，而且通过上面的nginx转发性能也有损耗。
于是在AI的帮助下，写了一套IPv4-IPv6-IPv4的程序，这里的协议是TCP
这样就可以转发1.7.2这样老版本的minecraft服务器的流量了




#### 软件架构
服务器:[IPv4->IPv6]-IPv6公网-[IPv6->IPv4]:客户端


#### 安装教程

使用Python运行
v2版本只能在windows里用

#### 使用说明

#服务器先对conf.json文件进行配置，然后重新运行
#然后服务器复制conf.json文件给客户端

#### 参与贡献
#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
