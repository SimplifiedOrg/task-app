import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from flask import Flask, redirect, render_template, request
from core.tasks import add_task, complete_task, delete_task, list_tasks

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", tasks=list_tasks())


@app.post("/add")
def add():
    add_task(request.form["title"], request.form["priority"], request.form["due"] or None)
    return redirect("/")


@app.post("/complete/<int:id>")
def complete(id):
    complete_task(id)
    return redirect("/")


@app.post("/delete/<int:id>")
def delete(id):
    delete_task(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
