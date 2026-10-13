class Pizza:
    __sizes_and_prices = {
        "Small":10,
        "Medium":12,
        "Large":14,
        "X_large":16
    }

    __topping = {"ham":0.5,
                 "sweetcorn":0.3,
                 "chicken":0.6,
                 "pepper":0.4}


    def __init__(self,topping,size="Medium"):
        self.__topping = topping


        if size.lower() in Pizza.__sizes_and_prices:
            self.size = size
        else:
            self.size = "Medium"

    @classmethod
    def new_size(cls,new_size):
        new_size = input("Enter new size:")
        cls.size = new_size
    @classmethod
    def validate_size(cls, new_size,price):
        if new_size not in Pizza:
            Pizza[new_size] =price
            return True
        return False

    def display(self):
        if len(self.__topping) == 0:
            print(f"{self.size} pizza with no toppings")
        else:
            print(f"{self.size} pizza with {",".join(self.__topping)} toppings")

    def get_size(self):
        return self.size

    def set_size(self,new_size):
        if new_size in Pizza.__sizes_and_prices:
            self.size = new_size
            return True
        else:
            return False
    def get_num_topping(self):
        return len(self.__topping)

    def add_topping(self,new_topping):
        self.__topping.append(new_topping)
        return True

    def remove_topping(self, topping):
        for existing_topping in self.__topping:
            if existing_topping.lower()== topping.lower():
                self.__topping.remove(existing_topping)
                return True
        return False
    def calc_price(self):
        base = Pizza.__sizes_and_prices[self.size]
        topping_price = self.get_num_topping()*0.85
        return base + topping_price

