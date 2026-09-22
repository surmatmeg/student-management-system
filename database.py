import json
import os

DB_FILE = "students.json"


def load_students():
  if not os.path.exists(DB_FILE):
    return []
  with open(DB_FILE, "r") as f:
    return json.load(f)


def save_students(students):
  with open(DB_FILE, "w") as f:
    json.dump(students, f, indent=4)