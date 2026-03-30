"""
This module contains all the core operations (CRUD) and statistics
for managing the inventory in memory.
"""

#This function allows me to add a student to my system.
def add_student(students, id, name, age, course, status):
    student = {
        "id": id,
        "name": name,
        "age": age,
        "course" : course,
        "status" : status
    }

    students.append(student)
    print("student added successfully.")

#This function allows me to see all registered students.
def show_students(students):

    if len(students) == 0:
        print("Is empty.")
    else:
        print("\n--- students summary ---")
        for p in students:
            print("id: ",p["id"], "| name:", p["name"], "| Age:", p["age"], "| Course: ", p["course"],"| Status: ", p["status"])

#This function allows me to search for a student by name.
def search_student(students, name):

    found = None

    for p in students:
        if p["name"] == name:
            found = p
    return found

#This function allows me to search for the student by name and update the information.
def update_student(students, name, new_age, new_course, new_status):

    student = search_student(students, name)

    if student != None:
        student["age"] = new_age
        student["course"] = new_course
        student["status"] = new_status
        
        print("student updated.")
    else:
        print("student not found.")

#This function allows me to search for a student by name and delete them.
def delete_student(students, name):

    student = search_student(students, name)

    if student != None:
        students.remove(student)
        print("student removed.")
    else:
        print("student not found.")

