from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    username = "admin"                        # change if you want
    password = "password"          # ← CHANGE THIS
    full_name = "Dimitris Klimenko"

    if User.query.filter_by(username=username).first():
        print("User already exists!")
    else:
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_pw, full_name=full_name)
        db.session.add(new_user)
        db.session.commit()
        print("User created successfully!")