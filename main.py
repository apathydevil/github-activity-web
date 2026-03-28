from flask import Flask, render_template, request
import fetcher

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/activity')
def activity():
    username = request.args.get('username')
    data = fetcher.fetch(username)
    if data is not None:
        processed = []
        for event in data:
            timestamp = event['created_at'].replace('T', ' ').replace('Z', '')
            if event['type'] == 'PushEvent':
                processed.append(f"Pushed to {event['repo']['name']} at {timestamp}")
            elif event['type'] == 'CreateEvent':
                processed.append(f"Created {event['payload']['ref_type']} in {event['repo']['name']} at {timestamp}")
            elif event['type'] == 'WatchEvent':
                processed.append(f"Starred {event['repo']['name']} at {timestamp}")
            elif event['type'] == 'ForkEvent':
                processed.append(f"Forked {event['repo']['name']} at {timestamp}")
            else:
                processed.append(f"{event['type']} in {event['repo']['name']} at {timestamp}")
        return render_template("activity.html", username=username, events=processed)
    else:
        return render_template("activity.html", username=username, events=["No data available."])

if __name__ == '__main__':
    app.run(debug=True)