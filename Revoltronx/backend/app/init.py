from flask import Flask

def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        from . import routes  # Import routes
        # You can also add database initialization here if needed
        
    return app
