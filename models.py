from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()  # initialize here, bind to app in app.py

# Project table model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.name}>'

# Optional: function to create database tables
def init_db(app):
    with app.app_context():
        db.create_all()
