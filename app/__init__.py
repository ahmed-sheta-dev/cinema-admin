from flask import Flask, jsonify

from app.common.errors import register_error_handlers


def create_app():
    app = Flask(__name__)

    
    #basic rout to verify app is working
    @app.get("/health")
    def index():
        return jsonify({"message": "App is running"}), 200
        

    register_error_handlers(app)

    return app