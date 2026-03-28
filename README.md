# flask-intro

This was my first ever Flask project, created as a learning exercise to understand the basics of web development with Flask. The application allows users to enter a GitHub username and view their recent activity, such as commits, pull requests, and issues. The fetching of GitHub data is done with the same code as in the [`github-activityCLI`](https://github.com/apathydevil/github-activityCLI) project, but here it's integrated into a web interface.

## Usage
1. `git clone https://github.com/apathydevil/github-activity-web`
2. `cd github-activity-web`
3. `pip install -r requirements.txt`
4. `python main.py`
5. Open your browser and navigate to `http://127.0.0.1:5000`