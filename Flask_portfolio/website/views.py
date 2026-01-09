from flask import Blueprint, render_template
from .modules import Project

views = Blueprint("views", __name__)

@views.route("/")
def home():
    projects = Project.query.all()
    return render_template("home.html", projects=projects)
