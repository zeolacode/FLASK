from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "Home"
    lista = ["nav", "container", "footer", "info"]
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/teste')
def index2():
    dic = {
        "interface": {
            "name": "GigabitEthernet1/1",
            "ip_address": "10.0.0.1/31",
            "description": "Uplink to core",
            "speed": "1000",
            "duplex": "full",
            "mtu": "9124"
        }
    }
    keys = dic['interface'].keys()
    return render_template('index2.html', dic=dic, keys=keys)


if __name__ == "__main__":
    app.run(debug=True)