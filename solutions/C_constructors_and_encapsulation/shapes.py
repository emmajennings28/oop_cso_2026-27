class Rectangle:
    def __init__(self, length, width, colour="Blue"):
        self.length = length
        self.width = width
        self.colour = colour

    def display(self):
        print(f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}]")

    def calc_area(self):
        return self.length * self.width


if __name__ == "__main__":
    rect1 = Rectangle(4.4, 2.2, "Red")

    print(f"Length: {rect1.length}")
    print(f"Width: {rect1.width}")
    print(f"Colour: {rect1.colour}")

    rect1.display()
    area = rect1.calc_area()
    print(f"The area of rect1 = {area}")