from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Project is LIVE on AWS EC2 🚀"

app.run(host="0.0.0.0", port=80)

