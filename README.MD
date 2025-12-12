-- base.html file--

1. This is the main file with the structure like a HOUSE.
2. All other pages like home or detail are just rooms inside this house.
3. Instead of building the same style etc, we build them once here in base.html.


----------------------------------------------------------------------------------------
### flask app logic

What the app does

* Shows all projects on the home page
* Lets you add a project with a simple form
* Shows project details on a separate page
* Uses URL routing to move between pages
* Uses HTML templates for the layout
* Uses a Python class (`Project`) to describe each project
* Creates a timestamp for every new project
* Redirects back to home after adding a project

## Routes

### `/`

Shows all projects.

### `/project/<project_id>`

Shows details for one project.
If the project does not exist, returns a 404 page.

### `/add_project`

Handles form submission.
Reads the project name and saves it.
Redirects to home.

### How to run

bash
python app.py

http://127.0.0.1:5000



If you want, I can also add installation steps, folder structure, or a screenshot section.

----------------------------------------------------------------------------------------

### sql connection 


Flask-SQLAlchemy lets Flask talk to SQLite.

The database file is stored in the instance/ folder.

SQLALCHEMY_DATABASE_URI tells Flask where the database file is.

db = SQLAlchemy(app) creates the database manager.

Project is the table model.

db.create_all() creates the database file and tables.

query.all() and get_or_404() read data.

db.session.add() + commit() write data.