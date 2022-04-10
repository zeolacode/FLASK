from flask import Flask, jsonify

app = Flask(__name__)

videos = [
    {
        "id": 1,
        "title": "1. - TESTE FLASK"
    },
        {
        "id": 2,
        "title": "2. - TESTE FLASK"
    }
]

youtube_videos = [
    {
        "id": 1,
        "title": "1. - TESTE FLASK"
    },
        {
        "id": 2,
        "title": "2. - TESTE FLASK"
    }
]

@app.route('/')
def index():

    return "Hello world!"

@app.route("/api/v1/videos/")
def get_all_videos():

    return jsonify({"midia": {"videos": videos, "youtube_videos": youtube_videos}})

if __name__ == "__main__":
    app.run(debug=True)