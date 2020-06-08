from flask import Flask, render_template, url_for
app = Flask(__name__)

notes = [
    {
        "title": "NOTES#1",
        "content": "test",
        "type": "primary"
    },
    {
        "title": "NOTES#2",
        "content": "testtoo",
        "type": "secondary"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", notes=notes, title="All notes")

if __name__ == "__main__":
    app.run(debug=True)