import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello, Ebryx CI/CD!"}

if __name__ == "__main__":
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    app.run(host=host, port=port)