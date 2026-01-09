from website import create_app, db
from website.modules import Project

app = create_app()

with app.app_context():

    projects = [
        {
            "title": "Flask Portfolio",
            "description": "Personal portfolio website built with Flask.",
            "tech_stack": "Flask, SQLAlchemy, HTML, CSS",
            "github_url": "https://github.com/yourname/flask-portfolio"
        },

        {
            "title": "Hangman",
            "description": "Terminal-based game following hangman's game logic",
            "tech_stack": "Python",
            "github_url": "https://github.com/Just3n0k/Coding-journey/tree/main/Hangman"
        },

        {
            "title": "Statistics solver",
            "description": "Terminal-based algorthim that follows math principals",
            "tech_stack": "Python",
            "github_url": "https://github.com/Just3n0k/Coding-journey/tree/main/Statistics%20solver"
        },

        {
            "title": "Webscraper",
            "description": "Scrapes 9Anime.com",
            "tech_stack": "Python",
            "github_url": "https://github.com/Just3n0k/Coding-journey/tree/main/WebScrape"
        },



    ]

    for p in projects:
        exists = Project.query.filter_by(title=p["title"]).first()
        if exists:
            print(f"Skipping duplicate: {p['title']}")
            continue

        project = Project(**p)
        db.session.add(project)

    db.session.commit()
    print("Projects added successfully.")
