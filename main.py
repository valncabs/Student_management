"""
Main application file.
Manages user interaction through a console menu, 
allowing CRUD operations to be performed on student information.

"""

from services import *
from file_manager import *


students = []
exit = False

while exit == False:

    print("\n--- MENU ---")
    print("1. Add student")
    print("2. Show inventory")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Save CSV")
    print("7. Load CSV")
    print("8. Exit")

    opcion = input("Select an option: ")

    # Add student
    if opcion == "1":
        status = ("asset", "idle")
        id = int(input("id: "))
        name = input("Name: ").lower()
        age = int(input("Age: "))
        course = input("Course: ")
        status = input("choice status (Assest/Idle): ")
        add_student(students, id, name, age, course, status)

    # Show students
    elif opcion == "2":
        show_students(students)
        

    # Search student
    elif opcion == "3":
        name = input("student name: ")
        p = search_student(students, name)

        if p != None:
            print("id: ",p["id"], "| name:", p["name"], "| Age:", p["age"], "| Course: ", p["course"],"| Status: ", p["status"])
        else:
            print("student not found.")

    # Update student
    elif opcion == "4":
        name = input("Student Name: ").lower()
        age = int(input("New Age: "))
        course = input("New Course: ")
        status = input("choice new status (Assest/Idle): " )
        update_student(students, name, age, course, status)


    # Delete student
    elif opcion == "5":
        name = input("student name: ")
        delete_student(students, name)



    # Save CSV
    elif opcion == "6":
        route = input("File path: ")
        save_csv(students, route)



    # Load CSV
    elif opcion == "7":
        route = input("File path: ")
        news = load_csv(route)

        decision = input("Overwrite current inventory? (S/N): ").lower()

        if decision == "S":
            students = news
        else:
            # Merge inventories
            for new in news:
                exists = search_student(students, new["name"])

                if exists != None:
                    # Update age, course and  and status
                    exists["age"] = new["age"]
                    exists["course"] = new["course"]
                    exists["status"] = new["status"]
                else:
                    students.append(new)

    # Exit program
    elif opcion == "8":
        exit = True
        print("Program finished.")

    else:
        print("Invalid option.")