from flask import Flask, render_template
app = Flask(__name__)

notes = [
    {
        "title": "NOTES#1",
        "content": "test"
    },
    {
        "title": "NOTES#2",
        "content": "testtoo"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)