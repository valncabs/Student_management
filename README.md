# Student Management System

## Description

This project is a student registration system developed in Python.

It allows the user to manage student information through basic operations such as adding, viewing, searching, updating, and deleting.

The program also works with CSV files to save and load data.

---

## Functionalities

* Add a student
* Show all students
* Search for a student
* Update student data
* Delete a student
* Save data to CSV
* Load data from CSV

---

## Project Structure

* main.py → Main program with menu
* services.py → Inventory functions (CRUD)
* file_manager.py → CSV file functions

---

## Data Structure

Each student is stored as follows:

student = { "id": id,
"name": name,
"age": age,
"course": course,
"status": status

}

---

## How to Run

1. Open the project folder.

2. Run the program:

python main.py and interact with the menu.

---


## CSV Format

The CSV file must be in this format. Format:

ID, name, age, course, status
1, valentina, 19, sst, inactive
2, luna, 56, en, active

---

