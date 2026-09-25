import unittest
import sqlite3
import database

class TestStudentDatabase(unittest.TestCase):

    def setUp(self):
        """Creates an in-memory SQLite database connection shared across functions."""
        # Create a single shared in-memory connection
        self.test_conn = sqlite3.connect(":memory:")
        
        # Override database.connect_db to always return our test connection
        database.connect_db = lambda: self.test_conn
        
        # Initialize the table inside our test connection
        database.initialize_db()

    def tearDown(self):
        """Closes the test connection after each test."""
        self.test_conn.close()

    def test_add_student(self):
        """Test adding a student to SQLite."""
        student_id = database.add_student("Alice", 20, "A")
        self.assertEqual(student_id, 1)

        student = database.search_student(1)
        self.assertIsNotNone(student)
        self.assertEqual(student[1], "Alice")
        self.assertEqual(student[2], 20)
        self.assertEqual(student[3], "A")

    def test_get_all_students(self):
        """Test fetching all student records."""
        database.add_student("Alice", 20, "A")
        database.add_student("Bob", 22, "B")

        students = database.get_all_students()
        self.assertEqual(len(students), 2)

    def test_delete_student(self):
        """Test deleting a student from SQLite."""
        student_id = database.add_student("Charlie", 21, "C")
        
        deleted = database.delete_student(student_id)
        self.assertTrue(deleted)

        student = database.search_student(student_id)
        self.assertIsNone(student)

if __name__ == "__main__":
    unittest.main()