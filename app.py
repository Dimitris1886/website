from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = "dev"


# ---------- HOME PAGE ----------
@app.route("/")
def home():
    projects = [
        {"id": 1, "name": "Project A", "color": "grey-medium"},
        {"id": 2, "name": "Project B", "color": "success"},
        {"id": 3, "name": "Project C", "color": "warning"},
        {"id": 4, "name": "Project D", "color": "danger"},
        {"id": 5, "name": "Project E", "color": "info"},
        {"id": 6, "name": "Project F", "color": "teal"},
        {"id": 7, "name": "Project G", "color": "purple"},
        {"id": 8, "name": "Project H", "color": "indigo"},
    ]
    return render_template("home.html", projects=projects)







# ---------- PROJECT DETAIL PAGE ---------- CHANGE ALL!!!!
@app.route("/project/<int:project_id>")
def project_detail(project_id):
    # Fake data for now
    project_names = {1: "Project A", 2: "Project B", 3: "Project C", 4: "Project D"}
    project_colors = {1: "primary", 2: "success", 3: "warning", 4: "danger"}

    if project_id not in project_names:
        return "Project not found", 404

    return render_template(
        "project_detail.html",
        project_id=project_id,
        name=project_names[project_id],
        color=project_colors[project_id]
    )


if __name__ == "__main__":
    app.run(debug=True)