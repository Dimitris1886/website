from models import db, Project


def create_project(name: str):
    name = name.strip()

    if not name:
        return False, "Project name cannot be empty."

        # Check for duplicate
    if Project.query.filter_by(name=name).first():
        return False, "A project with this name already exists."     
    
    project = Project(name=name)
    db.session.add(project)
    db.session.commit()
    
    return True, "Project created successfully."


def rename_project(project_id: int, new_name: str):
    new_name = new_name.strip()
    
    if not new_name:
        return False, "Project name cannot be empty."

    project = Project.query.get_or_404(project_id)

    # Check if the new name is different from current
    if new_name == project.name:
        return True, "Name unchanged (same as before)."

    # Check for duplicate 
    existing = Project.query.filter(
        Project.name == new_name,
        Project.id != project_id
    ).first()

    if existing:
        return False, "A project with this name already exists."

    project.name = new_name
    db.session.commit()
    
    return True, "Project renamed successfully."

def delete_project(project_id: int):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return True, "Project deleted successfully."
