from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = "dev"

# ONE SINGLE LIST — used by both home and detail page
PROJECTS = [
    {"id": 1, "name": "Project A", "color": "grey-medium"},
    {"id": 2, "name": "Project B", "color": "success"},
    {"id": 3, "name": "Project C", "color": "warning"},
    {"id": 4, "name": "Project D", "color": "danger"},
    {"id": 5, "name": "Project E", "color": "info"},
    {"id": 6, "name": "Project F", "color": "teal"},
    {"id": 7, "name": "Project G", "color": "purple"},
    {"id": 8, "name": "Project H", "color": "indigo"},
]

@app.route("/")
def home():
    return render_template("home.html", projects=PROJECTS)

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    # Find project in the same list
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    
    if project is None:
        return "Project not found", 404

    return render_template("project_detail.html",
                          name=project["name"],
                          color=project["color"])

if __name__ == "__main__":
    app.run(debug=True)