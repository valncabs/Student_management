"""
This module handles CSV file operations:
- Saving students to a file
- Loading students from a file
"""

import csv


def save_csv(students, route):

    if len(students) == 0:
        print("Is empty, cannot save.")
    else:
        try:
            archive = open(route, "w", newline="", encoding="utf-8")
            writer = csv.writer(archive)

            # Write header
            writer.writerow(["id", "name", "age", "course", "Status"])

            # Write product data
            for p in students:
                writer.writerow([p["id"], p["name"], p["age"], p["course"],p["status"]])

            archive.close()
            print("File saved at:", route)

        except:
            print("Error while saving file.")


def load_csv(route):
    """
    Loads inventorystudents data from a CSV file.
    Returns:
        list: list of valid students
    """
    students = []

    try:
        archive = open(route, "r", encoding="utf-8")
        reader = csv.reader(archive)

        # Read header
        header = next(reader)

        if header != ["id", "name", "age", "course", "Status"]:
            print("Invalid header.")
        else:
            for row in reader:
                # Validate number of columns
                if len(row) == 5:
                        id = int(row[0])
                        name = (row[1])
                        age = int(row[2])
                        course = row[3]
                        status = row[4]
                        student = {
                            "id": id,
                            "name": name,
                            "age": age,
                            "course" : course,
                            "status" : status
                            }
                        students.append(student)
                else:
                    print("error load")
        archive.close()
    except:
        print("ERROR")
    return students