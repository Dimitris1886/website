from flask import Flask
from models import db, init_db
from routes.projects import projects_bp

# Create Flask app
app = Flask(__name__)
app.secret_key = "dev"

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind database to app
db.init_app(app)
init_db(app)  # create tables if they don't exist

# Register Blueprints (after app is created)
app.register_blueprint(projects_bp)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
