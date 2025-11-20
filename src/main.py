import sys
import json
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from ai_chat.chat_engine import ChatEngine
from ai_browser.browser_engine import BrowserEngine
from ai_terminal.terminal_engine import TerminalEngine
from api_server.server import APIServer
from api_server.auth import authenticate_user
import config.settings as settings

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

chat_engine = ChatEngine()
browser_engine = BrowserEngine()
terminal_engine = TerminalEngine()
api_server = APIServer()

@app.route('/api/chat', methods=['POST'])
def chat():
    if not authenticate_user(request.headers.get('Authorization')):
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    response = chat_engine.process_message(data['message'])
    return jsonify({"response": response})

@app.route('/api/browser', methods=['POST'])
def browser():
    if not authenticate_user(request.headers.get('Authorization')):
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    response = browser_engine.analyze_page(data['url'])
    return jsonify({"summary": response})

@app.route('/api/terminal', methods=['POST'])
def terminal():
    if not authenticate_user(request.headers.get('Authorization')):
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json
    response = terminal_engine.execute_command(data['command'])
    return jsonify({"output": response})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
