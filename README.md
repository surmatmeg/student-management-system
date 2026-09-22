# Student Management System

A lightweight, console-based Student Management System built in Python with local JSON data persistence.

## Features
- **Add Student:** Create student records with automatic ID generation.
- **View All Students:** Display all registered students in a formatted list.
- **Search Student:** Quick search by student name or unique ID.
- **Delete Student:** Remove student records by ID.
- **Input Validation:** Prevents blank entries and invalid age inputs.
- **Data Persistence:** Automatically saves and loads data from `students.json`.

## Project Structure
- `main.py` - User interface and application control flow.
- `database.py` - Handles reading, writing, searching, and deleting data in JSON.
- `students.py` - Student object structure.
- `students.json` - Local data storage file (git-ignored).

## How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/surmatmeg/student-management-system.git](https://github.com/surmatmeg/student-management-system.git)
   cd student-management-system