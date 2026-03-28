import requests

def fetch(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for user '{username}'. Status code: {response.status_code}")
        return None
