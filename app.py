from flask import Flask
import subprocess
import json
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/json")
def hello_api_json():
    return {
        "message": "Hello, World!"
    }





@app.route("/api/add-user", methods=["POST"])
def add_user():
    username = request.json.get("username")
    email = request.json.get("email")
    return {
        "username": username,
        "email": email
    }
    

@app.route("/api/list-disks")
def list_disks():
    result = subprocess.run(['df', '-h'], capture_output=True, text=True)
    disks = result.stdout
    disks_json = json.loads(disks)
    return json.dumps(disks_json)


@app.route("/api/create-file", methods=["POST"])
def create_file():
    data = request.json
    filename = data.get("filename")
    content = data.get("content")

    subprocess.run(['echo', content, '>', filename], shell=True)

    return {
        "message": "File created successfully"
    }