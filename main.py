from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/activity')
def activity():
    username = request.args.get('username')
    return f"Showing activity for {username}"

if __name__ == '__main__':
    app.run(debug=True)