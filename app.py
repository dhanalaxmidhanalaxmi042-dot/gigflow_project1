from flask import Flask, render_template, request, redirect
import sqlite3

# Create Flask app
app = Flask(__name__)

# Function to connect to database
def get_db():
    return sqlite3.connect("gigflow.db")

# Home page – show all jobs
@app.route("/")
def home():
    db = get_db()
    jobs = db.execute("SELECT * FROM jobs").fetchall()
    db.close()
    return render_template("index.html", jobs=jobs)

# Post a job page
@app.route("/post", methods=["GET","POST"])
def post():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        db = get_db()
        db.execute("INSERT INTO jobs(title, desc) VALUES(?, ?)", (title, desc))
        db.commit()
        db.close()
        return redirect("/")
    return render_template("post.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)