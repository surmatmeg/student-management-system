from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# Ensure the database table exists when starting the web app
database.initialize_db()

@app.route("/")
def index():
    students = database.get_all_students()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    age = request.form.get("age")
    grade = request.form.get("grade")

    if name and age and grade:
        database.add_student(name, int(age), grade)

    return redirect(url_for("index"))

@app.route("/delete/<int:student_id>")
def delete(student_id):
    database.delete_student(student_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)