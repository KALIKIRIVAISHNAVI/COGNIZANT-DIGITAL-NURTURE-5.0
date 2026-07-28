from flask import Flask, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 47. Initialize extensions globally
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Connect extensions to app context
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 40. Register the Blueprint using your explicit app module name: HO5app
    from HO5app.routes import courses_bp
    app.register_blueprint(courses_bp)
    
    # Global fallbacks for clean JSON API errors
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify({'status': 'error', 'data': {'message': 'Resource not found.'}}), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({'status': 'error', 'data': {'message': 'Internal Server Error.'}}), 500
        
    return app

if __name__ == '__main__':
    application = create_app()
    application.run()