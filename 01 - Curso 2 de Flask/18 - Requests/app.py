from flask import Flask, render_template
from requests import get

app = Flask(__name__)

@app.route("/")
def index():

    return "Hello World!"

@app.route("/video")
def show_videos():

    videos = get("http://127.0.0.1:5000/api/v1/videos/").json()

    return videos["midia"]["videos"][0]["title"]

if __name__== "__main__":
    app.run(debug=True, port=3000)
