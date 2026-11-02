from subprocess import check_output


class Address:
    house_number = 100
    address_line1 = "Park Place"
    address_line2 = None
    address_line3 = None
    city = "Happyland"
    state = "Bliss"
    postcode = "K103958"
    country = "Ireland"

    def __init__(self, house_number, address_line1, city, state, postcode, country, address_line2=None, address_line3=None):
        self.house_number = house_number
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.address_line3 = address_line3
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country

    def display(self):
        print(f"{self.house_number} {self.address_line1}")
        if self.address_line2 is not None:
            print(self.address_line2)
        if self.address_line3 is not None:
            print(self.address_line3)
        print(self.city)
        print(self.state)
        print(self.postcode)
        print(self.country)


if __name__ == "__main__":
    address = Address(100, "Percy Lane", "Anaheim", "Florida", "Disneyworld", "USA", "Main Street")
    address.display()