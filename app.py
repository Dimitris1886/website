from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"

# data base connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# project table model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.name}>'
    
# create database / creates automatically in the folder instance
with app.app_context():
    db.create_all()


# routes
@app.route("/")
def home():
    projects = Project.query.order_by(Project.id).all()
    return render_template("home.html", projects=projects)


@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    if project is None:
        return "Project not found", 404
    return render_template("project_detail.html", name=project["name"])


# reads "name"
@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        name = request.form["name"].strip()
        if name:
            new_project = Project(name=name)
            db.session.add(new_project)
            db.session.commit()
        return redirect(url_for("home"))
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)