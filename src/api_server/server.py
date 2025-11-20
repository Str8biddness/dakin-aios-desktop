from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

class APIServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.limiter = Limiter(get_remote_address, app=self.app, default_limits=["100 per hour"])

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)
