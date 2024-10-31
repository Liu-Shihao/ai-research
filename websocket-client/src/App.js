import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

const App = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    // 连接到 WebSocket 服务器
    const socket = io('http://localhost:8080',{
        transports: ["websocket"]
    }); // 注意这里的端口号要和 Flask 端口一致

    // 监听 'log_message' 事件，并将消息添加到日志列表
    socket.on('log_message', (msg) => {
      setLogs((prevLogs) => [...prevLogs, msg.data]);
    });

    // 在组件卸载时断开连接
    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div className="App">
      <h1>Real-Time Logs</h1>
      <div>
        {logs.map((log, index) => (
          <p key={index}>{log}</p>
        ))}
      </div>
    </div>
  );
};

export default App;