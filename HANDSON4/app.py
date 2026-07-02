from flask import Flask, jsonify
from config import Config
from courses.routes import courses_bp

def create_app():
    # Initialize the app
    app = Flask(__name__)
    
    # Load configurations
    app.config.from_object(Config)

    # Register the Blueprint
    app.register_blueprint(courses_bp)

    # Task 2, Step 45: Custom JSON Error Handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({'error': 'Bad Request'}), 400

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()