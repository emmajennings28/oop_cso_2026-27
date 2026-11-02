from people import Person


if __name__ == "__main__":
    my_person = Person()

    if my_person.is_left:
        print(f"Name: {my_person.first_name} {my_person.last_name}")
    else:
        print(f"Name: {my_person.first_name.upper()} {my_person.last_name.upper()}")
    print(f"Age: {my_person.age}")

    p2 = Person()

    print()
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    age = int(input("Enter age: "))

    left_handed = input("Are you left-handed? (y/Y for yes, any other key for no)")
    if left_handed.lower() == "y":
        is_lefty = True
    else:
        is_lefty = False

    p2.first_name = first
    p2.last_name = last
    p2.age = age
    p2.is_left = is_lefty

    if p2.is_left:
        print(f"Name: {p2.first_name} {p2.last_name}")
    else:
        print(f"Name: {p2.first_name.upper()} {p2.last_name.upper()}")
    print(f"Age: {p2.age}")

    print("MY PERSON DETAILS: ")
    if my_person.is_left:
        print(f"Name: {my_person.first_name} {my_person.last_name}")
    else:
        print(f"Name: {my_person.first_name.upper()} {my_person.last_name.upper()}")
    print(f"Age: {my_person.age}")