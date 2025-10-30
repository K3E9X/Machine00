from flask import Flask
from flask_cors import CORS
from routes.api import api
import os

app = Flask(__name__)

# Configure CORS
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://localhost:5000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Register blueprints
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def index():
    return {
        "name": "Application Security Assessment API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/api/health",
            "questions": "/api/questions",
            "submit": "/api/submit",
            "export_template": "/api/export/template",
            "export_results": "/api/export/results",
            "stats": "/api/stats"
        }
    }


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True').lower() == 'true'

    app.run(host='0.0.0.0', port=port, debug=debug)
