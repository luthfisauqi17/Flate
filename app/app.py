from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    note_type = db.Column(db.String(60), nullable=False, default="primary")
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Note('{self.id}', '{self.title}', '{self.content}', '{self.note_type}', '{self.date_created}')"

@app.route("/")
@app.route("/home")
def home():
    notes = Note.query.all()
    return render_template("index.html", notes=notes, title="All notes")

@app.route("/new", methods=['GET', 'POST'])
def new_note():
    if request.method == "POST":
        new_note_title = request.form["new-note-title"]
        new_note_content = request.form["new-note-content"]
        new_note_type = request.form["new-note-type"]
        new_note = Note(title=new_note_title, content=new_note_content, note_type=new_note_type)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("new_note.html", title="New note")

@app.route("/delete/<note_id>")
def delete_note(note_id):
    Note.query.filter_by(id=note_id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/edit/<note_id>", methods=['GET', 'POST'])
def edit_note(note_id):
    if request.method == "POST":
        updated_note = Note.query.filter_by(id=note_id).first()
        updated_note.title = request.form["new-note-title"]
        updated_note.content = request.form["new-note-content"]
        updated_note.note_type = request.form["new-note-type"]
        db.session.commit()
        return redirect(url_for("home"))
    edit_note = Note.query.filter_by(id=note_id)
    return render_template("edit_note.html", edit_note = edit_note)

@app.route("/view/<note_id>")
def view_note(note_id):
    view_note = Note.query.filter_by(id=note_id)
    return render_template("view_note.html", view_note = view_note)

if __name__ == "__main__":
    app.run(debug=True)