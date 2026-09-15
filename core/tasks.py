import json
from pathlib import Path

FILE = Path(__file__).resolve().parents[1] / "tasks.json"


def _load():
    return json.loads(FILE.read_text())


def _save(tasks):
    FILE.write_text(json.dumps(tasks, indent=2) + "\n")


def list_tasks(status="todo"):
    tasks = _load()
    if status == "all":
        return tasks

    matching = []
    for task in tasks:
        if task["status"] == status:
            matching.append(task)
    return matching


def add_task(title, priority="medium", due=None):
    tasks = _load()

    next_id = 1
    for task in tasks:
        if task["id"] >= next_id:
            next_id = task["id"] + 1

    task = {
        "id": next_id,
        "title": title,
        "status": "todo",
        "priority": priority,
        "due": due,
    }
    tasks.append(task)
    _save(tasks)
    return task


def complete_task(id):
    tasks = _load()
    for task in tasks:
        if task["id"] == id:
            task["status"] = "done"
            _save(tasks)
            return task
    raise ValueError(f"No task with id {id}")


def delete_task(id):
    tasks = _load()

    remaining = []
    for task in tasks:
        if task["id"] != id:
            remaining.append(task)

    _save(remaining)
    return id
