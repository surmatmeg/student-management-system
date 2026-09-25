import sqlite3

DB_NAME = "students.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    """Creates the 'students' table if it doesn't exist."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade TEXT NOT NULL
            )
        """)
        conn.commit()

def add_student(name: str, age: int, grade: str) -> int:
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (name, age, grade)
        )
        conn.commit()
        return cursor.lastrowid

def get_all_students() -> list:
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, grade FROM students")
        return cursor.fetchall()

def search_student(student_id: int):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, grade FROM students WHERE id = ?", (student_id,))
        return cursor.fetchone()

def delete_student(student_id: int) -> bool:
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        return cursor.rowcount > 0