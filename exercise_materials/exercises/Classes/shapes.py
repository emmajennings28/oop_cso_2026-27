from operator import length_hint


class Rectangle:
    length = 5
    width = 4
    colour = "blue"

    def display(self):
        print(f"Rectangle [Length: {self.length} , width = {self.width}, colour = {self.colour}]")

    def calc_area(self):

if __name__ == "__main__":
    rectangle_1 = Rectangle()
    print(f"Length: {rectangle_1.length}")
    print(f"Width: {rectangle_1.width}")
    print(f"Colour: {rectangle_1.colour}")
    rectangle_1.display()