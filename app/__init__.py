from flask import Flask, app, jsonify
from sqlalchemy import text

from app.common.errors import register_error_handlers
from app.db.session import close_db, get_db
from app.extensions import engine
from app.modules.halls.routes import halls_bp
from app.modules.movies.routes import movies_bp


def create_app():
    app = Flask(__name__)

    # basic rout to verify app is working
    @app.get("/health")
    def health():
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return jsonify({"status": "ok", "db_ok": True}), 200
        except Exception as e:
            # Temporary debug to see the real reason
            return jsonify({"status": "ok", "db_ok": False, "db_error": str(e)}), 200

    register_error_handlers(app)
    app.register_blueprint(movies_bp)
    app.register_blueprint(halls_bp)

    app.teardown_appcontext(close_db)
    return app
