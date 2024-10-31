from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import time

"""
pip install flask flask-socketio
"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/analyze', methods=['POST'])
def send_log():
    data = request.json
    message = data.get('message', 'No message provided')
    print("start analyze...")
    # 通过 WebSocket 发送消息到前端
    # 通过子线程启动日志发送
    from threading import Thread
    Thread(target=send_log).start()
    return jsonify({"status": "Message sent", "message": message}), 200


# WebSocket 连接事件
@socketio.on('connect')
def handle_connect():
    print("Client connected")

def send_log():
    while True:
        # 示例日志信息
        log_message = f"Log info at {time.strftime('%Y-%m-%d %H:%M:%S')}"
        print(log_message)
        socketio.emit('log_message', {'data': log_message})
        time.sleep(5)  # 每隔5秒发送一次

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, allow_unsafe_werkzeug=True)