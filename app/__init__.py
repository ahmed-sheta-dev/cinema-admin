from flask import Flask, jsonify

from app.common.errors import register_error_handlers
from app.db.session import get_db
from app.extensions import engine


def create_app():
    app = Flask(__name__)

    
    #basic rout to verify app is working
    @app.get("/health")
    def health():
        # DB ping (MySQL example)
        try: 
            with engine.connect() as conn:
                conn.execute("SELECT 1")
            db_ok = True
        except:
            db_ok = False


        return jsonify({"status": "ok", "db_ok": db_ok}), 200


    register_error_handlers(app)

    return app