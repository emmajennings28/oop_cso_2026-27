from operator import length_hint
from traceback import print_tb


class Rectangle:
    length = 5
    width = 4
    colour = "blue"

    def display(self):
        print(f"Rectangle [Length: {self.length} , width = {self.width}, colour = {self.colour}]")

    def calc_area(self):
        return self.length * self.width


if __name__ == "__main__":
    rectangle_1 = Rectangle()
    print(f"Length: {rectangle_1.length}")
    print(f"Width: {rectangle_1.width}")
    print(f"Colour: {rectangle_1.colour}")
    rectangle_1.display()

    rectangles = []

    for i in range(2):
        print(f"Rectangle {i+1}")

        rectangle = Rectangle()

        rectangle.length = float(input("Enter length"))
        rectangle.width = float(input("Enter width"))
        rectangle.colour = input("Enter colour")

        rectangles.append(rectangle)

    largest_rectangle = rectangles[0]
    for rectangle in rectangles:
        if rectangle.calc_area() > largest_rectangle.calc_area():
            largest_rectangle = rectangle

    print("The largest rectangle area is:")
    largest_rectangle.display()
    print(f"Area: {largest_rectangle.calc_area()}")


    smallest_width = rectangles[0].width
    smallest_position = 0

    for i in range(len(rectangles)):
        if rectangles[i].width < smallest_width:
            smallest_width = rectangles[i].width
            smallest_position = i

    print("Rectangle with the smallest width:")
    print(f"Position in list: {smallest_position}")

    red_rectangles = []

    for rectangle in rectangles:
        if rectangle.colour.lower() == "red":
            red_rectangles.append(rectangle)

    if len(red_rectangles) > 0:
        print("Red rectangles:")

        for rectangle in red_rectangles:
            rectangle.display()
    else:
        print("There is no red rectangles")