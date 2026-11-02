class Pizza:
    __sizes_and_prices:dict[str,float|int] = {
        "small":10,
        "medium":12,
        "large":14,
        "x_large":16
    }

    __topping_prices:dict[str,float|int]= {
            "ham":0.4,
            "sweetcorn":0.2,
    def __init__(self,toppings: dict,size:str="medium"):        self.__topping = []
        for t in toppings:
            self.add_topping(t)


        if size.lower() in Pizza.__sizes_and_prices:
            self.size = size
        else:
            self.size = "medium"

    @classmethod
    def is_valid_size(cls, size)-> str:
        return size.lower() in Pizza.__sizes_and_prices

    @classmethod
    def get_sizes(cls)-> dict [str,int]:
        return dict(Pizza.__sizes_and_prices)

    @classmethod
    def new_size(cls)-> None:
        new_size = input("Enter new size:")
        cls.size = new_size

    @classmethod
    def add_size(cls, size, price)-> None:
        size = size.lower()
        if size not in cls.__sizes_and_prices:
            cls.__sizes_and_prices[size] = price
            return True
        return False
    @classmethod
    def is_valid_topping(cls, topping)-> str:
        return topping.lower() in Pizza.__topping_prices
    @classmethod
    def get_topping_menu(cls)-> dict:
        return dict(Pizza.__topping_prices)

    def display(self)-> None:
        if not self.__topping:
            print(f"{self.size} pizza with no toppings")
        else:
            print(f"{self.size} pizza with {",".join(self.__topping)} toppings")

    def get_toppings(self)-> list:
        return list(self.__topping)

    def get_size(self)-> str:
        return self.size

    def set_size(self,new_size)->bool:
        if new_size in Pizza.__sizes_and_prices:
            self.size = new_size
            return True
        return False
    def get_num_topping(self)-> str:
        return len(self.__topping)

    def add_topping(self,new_topping)-> bool
        new_topping = new_topping.lower()
        if self.is_valid_topping(new_topping) and new_topping not in self.__topping:
            self.__topping.append(new_topping)
            return True
        return False


    def remove_topping(self, topping)->bool:
        topping = topping.lower()
        for topping in self.__topping:
            self.__topping.remove(topping)
            return True
        return False
    def calc_price(self)-> float:
        base = Pizza.__sizes_and_prices[self.size]
        topping_price: int =sum(Pizza.__topping_prices[t]for t in self.__topping)
        return base + topping_price



class Orders:
    def __int__(self,username: str) -> None:
        self.__username: str = username
        self.__pizzas: dict[str, Pizza] = {}

    def get_username(self) ->str:
        return self.__username

    def get_pizzas(self) -> dict[str,Pizza]:
        return dict(self.__pizzas)

    def add_pizza(self,nickname: str, new_pizza:Pizza) -> bool:
        if nickname in self.__pizzas:
            return False
        self.__pizzas[nickname] = new_pizza
        return True
    def get_pizza(self,nickname: str) -> Pizza | None:
        return self.__pizzas.get(nickname)
    def remove_pizza(self,nickname: str)-> Pizza | None:
        return self.__pizzas.pop(nickname, None)
    def calculate_total(self) -> float:
        return sum(pizza.calc_price() for pizza in self.__pizzas.values())
    def create_receipt(self)->str:
        lines=[f"order summary for {self.__username}"]
        if not self.__pizzas:
            lines.append("you havent ordered any pizzas")
        else:
            for nickname, pizza in self.__pizzas.items():
                toppings = ", ".join(pizza.get_toppings()) or "no toppings"
                lines.append(
                    f"{nickname}: {pizza.get_size()} pizza with {toppings} "
                    f" €{pizza.calc_price():.2f}"
                )

            lines.append(f"{self.__username}'s total bill is €{self.calculate_total():.2f}")
            return "\n".join(lines)

        def display_order(self) -> None:
            print(self.create_receipt())