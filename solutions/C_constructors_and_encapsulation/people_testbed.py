from people import Person


def display_person(person):
    if person.is_left:
        print(f"Name: {person.first_name} {person.last_name}")
    else:
        print(f"Name: {person.first_name.upper()} {person.last_name.upper()}")
    print(f"Age: {person.age}")


if __name__ == "__main__":
    my_person = Person("Dolly", "Madison", 187, False)

    display_person(my_person)

    print()
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    age = int(input("Enter age: "))

    left_handed = input("Are you left-handed? (y/Y for yes, any other key for no)")
    if left_handed.lower() == "y":
        is_lefty = True
    else:
        is_lefty = False

    p2 = Person(first, last, age, is_lefty)

    display_person(p2)

    print("MY PERSON DETAILS: ")
    display_person(my_person)