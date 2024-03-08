# Slides Share App

A web app for sharing lecture notes.

## Getting Started

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Guide
1. Create a virtual environment
    `python -m venv <name of environment>`
2. cd into project and install requirements
    `pip install -r requirements.txt`
3. Start the application by running
    `uvicorn app.main:app --reload`
4. visit http://localhost:8000/docs to view the swagger dev page.

## NB: Database file will be generated automatically when script is run.
## default Admin username and password is 
    username: admin
    password: password