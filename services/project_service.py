from models import db, Project

def create_project(name: str):
    name = name.strip()
    if not name:
        return None
    project = Project(name=name)
    db.session.add(project)
    db.session.commit()
    return project

def rename_project(project_id: int, new_name: str):
    project = Project.query.get_or_404(project_id)
    new_name = new_name.strip()
    if new_name:
        project.name = new_name
        db.session.commit()
    return project

def delete_project(project_id: int):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
