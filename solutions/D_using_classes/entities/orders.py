
class Pizza:
    _base_prices:dict[str, float] = {
        "small": 10,
        "medium": 12,
        "large" : 15,
        "extra_large" : 18
    }
    _topping_unit_price: float = 0.85

    def __init__(self, toppings: list[str], size: str="medium"):
        if size.lower() in Pizza._base_prices:
            self._size = size
        else:
            self._size = "medium"

        self.toppings = toppings

    @classmethod
    def validate_size(cls, size: str) -> bool:
        if size.lower() in cls._base_prices:
            return True

        return False

    @classmethod
    def add_valid_size(cls, new_size: str) -> bool:
        if new_size.lower() not in cls._base_prices:
            cls._sizes.append(new_size.lower())
            return True

        return False

    def set_size(self, new_size: str) -> bool:
        if new_size.lower() in Pizza._base_prices:
            self._size = new_size
            return True
        else:
            return False

    def get_size(self) -> str:
        return self._size

    def get_num_toppings(self) -> int:
        return len(self.toppings)

    def display(self) -> None:
        if len(self.toppings) == 1:
            toppings = self.toppings[0]
        elif len(self.toppings) > 1:
            toppings = ", ".join(self.toppings[0:-1])
            toppings += f" and {self.toppings[-1]}"
        else:
            toppings = "no toppings."

        print(f"{self._size} pizza with {toppings}")

    def add_topping(self, new_topping: str) -> bool:
        if not new_topping:
            return False

        self.toppings.append(new_topping.lower())
        return False

    def remove_topping(self, topping_to_remove: str) -> bool:
        if not topping_to_remove:
            return False

        topping_to_remove = topping_to_remove.lower()

        if topping_to_remove in self.toppings:
            self.toppings.remove(topping_to_remove)
            return True

        return False

    def calc_price(self) -> float:
        base_price = Pizza._base_prices[self._size]
        topping_price = len(self.toppings) * Pizza._topping_unit_price

        return base_price + topping_price


if __name__ == "__main__":
    pizza1 = Pizza(["cheese", "pineapple"], "medium")
    pizza1.display()

    pizza2 = Pizza(["hame, cheese", "pineapple"], "medium")
    pizza2.display()

    pizza3 = Pizza(["cheese"], "medium")
    pizza3.display()

    pizza4 = Pizza([], "medium")
    pizza4.display()

    updated_size = "personal"
    if pizza1.validate_size(updated_size):
        print(f"{updated_size} is a valid size")
    else:
        print(f"{updated_size} is invalid")

    if Pizza.validate_size(updated_size):
        print(f"{updated_size} is a valid size")
    else:
        print(f"{updated_size} is invalid")