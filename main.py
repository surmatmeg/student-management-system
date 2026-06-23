print("=================================")
print("   STUDENT MANAGEMENT SYSTEM")
print("=================================")

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        students.append({"name": name, "age": age})
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nList of Students:")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']} - Age {student['age']}")

    elif choice == "3":
        print("Exiting system... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
