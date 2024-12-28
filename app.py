from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App"
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    return f"Login attempted by {username}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
