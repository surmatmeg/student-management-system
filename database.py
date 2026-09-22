import json
import os

FILE_NAME = "students.json"


def load_students():
  """Loads students from the JSON file."""
  if not os.path.exists(FILE_NAME):
    return []
  with open(FILE_NAME, "r") as file:
    return json.load(file)


def save_students(students):
  """Saves the student list into the JSON file."""
  with open(FILE_NAME, "w") as file:
    json.dump(students, file, indent=4)


def search_student(query):
  """Searches for students by name or ID."""
  students = load_students()
  results = []
  query_str = str(query).lower()

  for student in students:
    if query_str in str(student["id"]) or query_str in student["name"].lower():
      results.append(student)

  return results


def delete_student(student_id):
  """Deletes a student by ID.

  Returns True if deleted, False if not found.
  """
  students = load_students()
  initial_length = len(students)

  # Keep all students EXCEPT the one with the matching ID
  updated_students = [s for s in students if s["id"] != student_id]

  if len(updated_students) < initial_length:
    save_students(updated_students)
    return True
  return False