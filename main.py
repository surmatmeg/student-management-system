from database import (
    add_student,
    delete_student,
    init_db,
    load_students,
    search_student,
)


def get_valid_age():
  """Helper function to keep asking until the user enters a valid positive age."""
  while True:
    age_input = input("Enter student age: ").strip()
    if age_input.isdigit() and int(age_input) > 0:
      return int(age_input)
    print("⚠️ Invalid age! Please enter a positive number (e.g., 20).")


def get_valid_name():
  """Helper function to keep asking until the user enters a non-empty name."""
  while True:
    name_input = input("Enter student name: ").strip()
    if name_input:
      return name_input
    print("⚠️ Name cannot be blank! Please enter a valid name.")


def main():
  init_db()  # Initialize SQLite table on application launch

  while True:
    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM  ")
    print("==============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter choice (1-5): ").strip()

    if choice == "1":
      name = get_valid_name()
      age = get_valid_age()
      new_id = add_student(name, age)
      print(f"✅ Success: '{name}' added with ID #{new_id} in SQLite database!")

    elif choice == "2":
      students = load_students()
      if not students:
        print("⚠️ No student records found.")
      else:
        print("\n--- List of Students ---")
        for s in students:
          print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']}")

    elif choice == "3":
      query = input("Enter student name or ID to search: ").strip()
      results = search_student(query)

      if not results:
        print(f"⚠️ No records matching '{query}'.")
      else:
        print(f"\n--- Search Results for '{query}' ---")
        for s in results:
          print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']}")

    elif choice == "4":
      id_input = input("Enter student ID to delete: ").strip()
      if not id_input.isdigit():
        print("⚠️ Please enter a valid numeric ID.")
        continue

      student_id = int(id_input)
      if delete_student(student_id):
        print(f"✅ Student ID #{student_id} deleted successfully!")
      else:
        print(f"⚠️ Student ID #{student_id} not found.")

    elif choice == "5":
      print("Exiting system. Goodbye!")
      break
    else:
      print("⚠️ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
  main()