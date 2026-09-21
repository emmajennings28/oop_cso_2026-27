if __name__ == "__main__":
    students = [
        {"name": "Annie", "average_mark": 55},
        {"name": "Aine", "average_mark": 39},
        {"name": "Mira", "average_mark": 66},
        {"name": "Dan", "average_mark": 47}
    ]

    # Answer for A1.1:
    for i in range(len(students)):
        print(f"Student name: {students[i]["name"]}")
        print(f"Average score: {students[i]["average_mark"]}")

    # Answer(s) for A1.2:
    # If we don't know where "Dan" is:
    for student_dict in students:
        if student_dict["name"] == "Dan":
            print(f"Dan's average mark: {student_dict["average_mark"]}")

    # If we know which position "Dan" is in:
    print(f"Dan's average mark: {students[3]["average_mark"]}")

    # Answer for A2:
    for student in students:
        if student["average_mark"] >= 50:
            print(student["name"])

    # Answer for A3:
    max_mark = -1
    name = None
    for i in range(len(students)):
        if students[i]["average_mark"] > max_mark:
            max_mark = students[i]["average_mark"]
            name = students[i]["name"]

    print(f"Student with highest mark ({max_mark}) was {name}")