from shapes import Rectangle
import random


def find_greatest_area(rect_list):
    max_area = -1
    biggest = None

    for rect in rect_list:
        if rect.calc_area() > max_area:
            max_area = rect.calc_area()
            biggest = rect

    return biggest

def find_min_width(rect_list):
    if not rect_list:
        return None

    min_width = rect_list[0].width
    smallest = None

    for rect in rect_list:
        if rect.width < min_width:
            min_width = rect.width
            smallest = rect

    return smallest


if __name__ == "__main__":
    rectangles = []

    for i in range(5):
        # Take in details for new Rectangle
        length = float(input(f"Enter length of rectangle {(i+1)}: "))
        width = float(input(f"Enter width of rectangle {(i + 1)}: "))

        # Generate a random number between 1 and 10
        rand = random.randint(1, 10)
        print(f"Random value generated = {rand}")
        # If random value is even, request colour from user
        if rand % 2 == 0:
            colour = input(f"Enter colour of rectangle {(i + 1)}: ")
            # Create rectangle with that data (including colour):
            rect = Rectangle(length, width, colour)
        else:
            print("Using default colour")
            # Create rectangle with length and width, using default colour
            rect = Rectangle(length, width)

        # Save rectangle in the list
        rectangles.append(rect)

    max_rect = find_greatest_area(rectangles)
    if max_rect is not None:
        print("Rectangle with greatest area:")
        max_rect.display()

    min_rect = find_min_width(rectangles)
    if min_rect is not None:
        print("Rectangle with smallest width:")
        min_rect.display()