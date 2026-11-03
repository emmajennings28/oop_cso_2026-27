class Rectangle:
    length = 10
    width = 5
    colour = "blue"

    def display(self):
        print(f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}]")

    def calc_area(self):
        return self.length * self.width

    def __str__(self) -> str:
        return f"The rectangle is{self.length} by {self.width} and the colour {self.colour}"

    def __repr__(self) -> str:
        return f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}"

    def __format__(self, format_spec: str) -> str:
        match format_spec.lower():
            case "simple":
                return f"{self.length} by {self.width} and colour {self.colour}"
            case "file":
                return f"{self.length}%%{self.width}%%{self.colour}"
            case _:
                return str(self)

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Rectangle):
            return NotImplemented
        if self.length != other.length:
            return False
        if self.width != other.width:
            return False
        if self.colour.lower() != other.colour.lower():
            return False

        return True

    def __ne__(self, other: object) -> bool | NotImplementedType:
        return not self == other

    def __hash__(self) -> int:
        return hash((self.length, self.width, self.colour))
if __name__ == "__main__":
    rect1 = Rectangle()

    print(f"Length: {rect1.length}")
    print(f"Width: {rect1.width}")
    print(f"Colour: {rect1.colour}")

    rect1.display()
    area = rect1.calc_area()
    print(f"The area of rect1 = {area}")