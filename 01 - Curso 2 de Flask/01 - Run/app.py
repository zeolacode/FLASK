from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print(__name__)
    return "Hello World!!!"

if __name__ == "__main__":
    # debug ativado 
    # port = xxx
    # host = "0.0.0.0"
    app.run(debug=True)