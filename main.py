from flask import Flask, jsonify, render_template

app = Flask(__name__)

dictionary = [
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
    ]


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/home", methods=["GET", "POST"])
def home():

    return render_template("index.html", data=dictionary, mainHeader="Hey there")


@app.route("/ikea/store/1")
def ikea():
    dictionary = [
        {
            'id': 1,
            'name': "Store 1",
            'location': "DC"
        },
    ]
    return jsonify(store=dictionary)


if __name__ == '__main__':
    app.run(debug=True)
