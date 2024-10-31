# NodeJS

如果 Node.js 已安装，你将会看到 Node.js 的版本号（例如：v18.12.0）。如果没有安装，会显示 “command not found” 错误。
npm 是 Node.js 的包管理器，一般会随 Node.js 一起安装。输入以下命令查看 npm 版本：
在终端输入以下命令：
```shell
# 检查 Node.js 和 npm 版本
node -v
npm -v

# 切换回官方的 npm 注册表
npm config set registry https://registry.npmjs.org/
npm config set registry https://registry.npmmirror.com/

# 切换成功后，可以用下面的命令检查当前的镜像地址是否正确
npm config get registry


# 更新 npm 到最新版本
npm install -g npm

#设置临时禁用严格 SSL 校验
npm config set strict-ssl false

#重置 npm 缓存
npm cache clean --force

# npx create-react-app websocket-client 是一个用于快速创建 React 项目的命令
npx create-react-app websocket-client

npm install socket.io-client

cd websocket-client
npm start

```
运行 npx create-react-app websocket-client 命令后，将会在当前目录创建一个名为 websocket-client 的 React 项目文件夹。这个文件夹内包含所有所需的文件和依赖，你可以直接进入该文件夹，启动开发服务器来运行 React 应用。

•	npx：这是 Node.js 提供的一个工具，用于运行 npm 包中的命令。如果你有 Node.js 安装在系统上，通常会自带 npx。

•	create-react-app：这是一个官方的 React 脚手架工具，用于生成 React 项目的基础模板，包括项目结构、配置文件和开发环境，帮助开发者快速上手 React 项目。

•	websocket-client：这是项目的名称。使用这个命令后，create-react-app 将会在当前目录下创建一个名为 websocket-client 的文件夹，并在里面生成 React 项目。


# Error
```shell
127.0.0.1 - - [31/Oct/2024 22:04:13] "GET /socket.io/?EIO=4&transport=polling&t=dmpunp3w HTTP/1.1" 400 -
127.0.0.1 - - [31/Oct/2024 22:04:18] "GET /socket.io/?EIO=4&transport=polling&t=dmtpxyd3 HTTP/1.1" 400 -
127.0.0.1 - - [31/Oct/2024 22:04:23] "GET /socket.io/?EIO=4&transport=polling&t=dmxkz0hk HTTP/1.1" 400 -
127.0.0.1 - - [31/Oct/2024 22:04:28] "GET /socket.io/?EIO=4&transport=polling&t=dn1gbxsh HTTP/1.1" 400 -
```
1. 确保 Flask-SocketIO 和 Socket.IO 客户端版本兼容
```shell
pip install flask-socketio
npm install socket.io-client@4
```
2. 在后端启用 WebSocket 支持
确保 Flask-SocketIO 服务器的 WebSocket 协议已正确配置。
```shell
from flask_socketio import SocketIO

# 启用 WebSocket 支持
socketio = SocketIO(app, cors_allowed_origins="*")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, allow_unsafe_werkzeug=True)
```
这里的 cors_allowed_origins="*" 允许所有跨域请求，适合开发环境。也可将其设为前端地址，如 http://localhost:3000。

3. 检查客户端的连接代码
在客户端连接 WebSocket 时，明确指定 transports 选项为 websocket，避免使用 polling：
```shell
const socket = io("http://localhost:5001", {
  transports: ["websocket"]
});
```