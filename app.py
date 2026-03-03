from flask import Flask
import datetime
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "1.0")

@app.route("/")
def home():
    return "version 2 deployed"
    return "version 2 deployed"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/time")
def time():
    return {"server_time": str(datetime.datetime.now())}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)