from . import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    tech_stack = db.Column(db.String(200), nullable=False)
    github_url = db.Column(db.String(300))
