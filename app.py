from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Jenkins Pipeline 🚀. Rev 0.1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
