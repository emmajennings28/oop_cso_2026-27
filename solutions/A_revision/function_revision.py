# Answer for B1:
def calc_average(marks):
    total = sum(marks)
    return round(total/len(marks), 2)

# Answer for B4:
def add_mark(student_dict, new_mark):
    student_dict["marks"].append(new_mark)

# "Helper" function - so I don't have to keep searching "manually"
def find_student(students_list, student_name):
    for student_dict in students_list:
        if student_dict["name"] == student_name:
            return student_dict

    return None


if __name__ == "__main__":
    students = [
        {"name": "Evan", "marks": [65, 72, 81]},
        {"name": "Caleb", "marks": [45, 51, 48]},
        {"name": "Angelo", "marks": [82, 77, 91]},
        {"name": "Dorothy", "marks": [55, 63, 59]}
    ]

    # Answer for B2.1:
    for student in students:
        print(f"{student["name"]}'s average mark: {calc_average(student["marks"])}%")

    print("-------------------------")

    # Answer for B2.2 (if we know where Caleb is in the list):
    print(f"Caleb's average mark: {calc_average(students[1]["marks"])}%")

    print("-------------------------")

    # Answer for B2.2 (if we don't know where Caleb is, or if he's even there)
    caleb = find_student(students, "Caleb")
    if caleb is not None:
        print(f"Caleb's average mark: {calc_average(caleb["marks"])}%")
    else:
        print("Caleb was not found in this student cohort")

    print("-------------------------")

    # Answer for B3:
    print("Students with an average of 50% or higher:")
    for student in students:
        if calc_average(student["marks"]) >= 50:
            print(f"{student["name"]}")

    print("-------------------------")

    # Testing for B4:
    print("Add 66 to Dorothy:")
    dorothy = find_student(students, "Dorothy")
    if dorothy is not None:
        add_mark(dorothy, 66)
        print(f"Dorothy's marks are now: {dorothy["marks"]}")
        print(f"Dorothy's average is now: {calc_average(dorothy["marks"])}")
    else:
        print("Dorothy was not found in this student cohort")
