from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>GitHub Activity Viewer</h1><p>Welcome!</p>"

if __name__ == '__main__':
    app.run(debug=True)