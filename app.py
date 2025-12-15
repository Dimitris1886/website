from flask import Flask
from flask_login import LoginManager
from models import db, init_db
from routes.projects import projects_bp
from routes.auth import auth_bp, login_manager  

app = Flask(__name__)
app.secret_key = "dev"  # change to something random in production!

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Flask-Login setup
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # redirect here if not logged in
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "warning"

# Register blueprints
app.register_blueprint(projects_bp)
app.register_blueprint(auth_bp)  

# Create tables
init_db(app)

if __name__ == "__main__":
    app.run(debug=True)