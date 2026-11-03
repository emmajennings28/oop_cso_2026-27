
class Pizza:
    _base_prices:dict[str, float] = {
        "small": 10,
        "medium": 12,
        "large" : 15,
        "extra_large" : 18
    }
    _TOPPING_UNIT_PRICE: float = 0.85

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

    def as_text(self) -> str:
        if len(self.toppings) == 1:
            toppings = self.toppings[0]
        elif len(self.toppings) > 1:
            toppings = ", ".join(self.toppings[0:-1])
            toppings += f" and {self.toppings[-1]}"
        else:
            toppings = "no toppings."

        return f"{self._size} pizza with {toppings} - €{self.calc_price()}"

    def display(self) -> None:
        print(self.as_text())

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
        topping_price = len(self.toppings) * Pizza._TOPPING_UNIT_PRICE

        return base_price + topping_price


class Order:
    def __init__(self, username: str):
        if not username:
            username = "AnnieBob"

        self._username = username
        self._pizzas: dict[str, Pizza] = {}

    def add_pizza(self, nickname: str, pizza: Pizza) -> bool:
        if not nickname:
            print("Cannot add a pizza with a blank nickname")
            return False

        nickname = nickname.lower()

        if nickname in self._pizzas:
            print("Nickname already present in order")
            return False

        self._pizzas[nickname] = pizza
        return True

    def get_pizza(self, nickname: str) -> Pizza | None:
        if not nickname:
            print("Cannot search for Pizza with blank nickname")
            return None

        nickname = nickname.lower()

        if nickname not in self._pizzas:
            return None

        return self._pizzas[nickname]

    def remove_pizza(self, nickname: str) -> Pizza | None:
        removed = self.get_pizza(nickname)

        if removed:
            del self._pizzas[nickname]

        return removed

    def calc_total(self) -> float:
        order_total = 0
        for pizza in self._pizzas.values():
            order_total += pizza.calc_price()

        return order_total

    def create_receipt(self) -> str:
        receipt_text = "-"*20
        receipt_text += "\n"
        receipt_text += f"Order for {self._username}\n"
        receipt_text += "-" * 20
        receipt_text += "\n"

        for i, pizza in enumerate(self._pizzas.values(), 1):
            receipt_text += f"{i}) {pizza.as_text()}\n"

        receipt_text += "\n"
        receipt_text += f"Total for order: €{self.calc_total()}"

        return receipt_text

    def display(self) -> None:
        print(self.create_receipt())


if __name__ == "__main__":
    pizza1 = Pizza(["cheese", "pineapple"], "medium")
    pizza1.display()

    pizza2 = Pizza(["ham", "cheese", "pineapple"], "small")
    pizza2.display()

    pizza3 = Pizza(["cheese"], "large")
    pizza3.display()

    pizza4 = Pizza([], "medium")
    pizza4.display()

    order = Order("Angelina")
    order.add_pizza("pineapple", pizza1)
    order.add_pizza("hawaiian", pizza2)
    order.add_pizza("cheeeeeese", pizza3)
    order.add_pizza("empty", pizza4)

    order.display()