from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
app.secret_key = "dev"

# ONE SINGLE LIST — all projects (no color anymore)
PROJECTS = [
    {"id": 1, "name": "Project A"},
    {"id": 2, "name": "Project B"},
    {"id": 3, "name": "Project C"},
    {"id": 4, "name": "Project D"},
    {"id": 5, "name": "Project E"},
    {"id": 6, "name": "Project F"},
    {"id": 7, "name": "Project G"},
    {"id": 8, "name": "Project H"},
]

@app.route("/")
def home():
    return render_template("home.html", projects=PROJECTS)

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if project is None:
        return "Project not found", 404
    return render_template("project_detail.html", name=project["name"])

# ← FIXED: only reads "name", no "color" → no more error!
@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        name = request.form["name"].strip()
        if name:  # don't allow empty names
            new_project = {
                "id": max(p["id"] for p in PROJECTS) + 1,
                "name": name
            }
            PROJECTS.append(new_project)
        return redirect(url_for("home"))
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)