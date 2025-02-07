from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! Welcome to your Flask app on Azure VM."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
