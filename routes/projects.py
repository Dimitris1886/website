from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Project

# Create Blueprint
projects_bp = Blueprint('projects', __name__)

# Home route – list all projects
@projects_bp.route("/")
def home():
    projects = Project.query.order_by(Project.id).all()
    return render_template("home.html", projects=projects)


# Project detail route
@projects_bp.route("/project/<int:project_id>")
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template("project_detail.html", project=project)


# Add new project
@projects_bp.route("/add_project", methods=["POST"])
def add_project():
    name = request.form.get("name", "").strip()
    if name:
        new_project = Project(name=name)
        db.session.add(new_project)
        db.session.commit()
    return redirect(url_for("projects.home"))


#  rename project
@projects_bp.route("/project/<int:project_id>/rename", methods=["POST"])
def rename_project(project_id):
    project = Project.query.get_or_404(project_id)
    new_name = request.form.get("name", "").strip()
    if new_name:
        project.name = new_name
        db.session.commit()
    return redirect(url_for("projects.project_detail", project_id=project.id))


# Delete project
@projects_bp.route("/project/<int:project_id>/delete", methods=["POST"])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("projects.home"))
