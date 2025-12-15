from flask import Blueprint, render_template, request, redirect, url_for
from models import Project
from services.project_service import create_project, rename_project, delete_project

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
    name = request.form.get("name", "")
    create_project(name)
    return redirect(url_for("projects.home"))

# Rename project
@projects_bp.route("/project/<int:project_id>/rename", methods=["POST"])
def rename_project_route(project_id):
    new_name = request.form.get("name", "")
    rename_project(project_id, new_name)
    return redirect(url_for("projects.project_detail", project_id=project_id))

# Delete project
@projects_bp.route("/project/<int:project_id>/delete", methods=["POST"])
def delete_project_route(project_id):
    delete_project(project_id)
    return redirect(url_for("projects.home"))
