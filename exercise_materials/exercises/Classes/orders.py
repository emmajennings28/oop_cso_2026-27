class Pizza:
    size_and_price = {
        "small" :10,
        "medium" :12,
        "large" : 14,
        "x_large" :16
    }

    __toppings = {}

    def __init__(self,toppings, size="Medium"):
        self.__toppings = toppings

        if size in self.size_and_price:
            self.__size = size
        else:


            self.__size = "Medium"

    def display(self):
        if len(self.__toppings) == 0:
            print(self.__size + "pizza with no toppings")
        else:
            print(self.__size + "pizza with" + ",".join(self.__toppings)+"toppings")

    def get_size(self):
        return self.__size
    def set_size(self,new_size):
        if new_size in self.size_and_price:
            self.__size = new_size
            return True
        else:
            return False
    def get_num_topping(self):
        return len(self.__toppings)

    def add_topping(self,new_topping):
        self.__toppings.append(new_topping)
        return True


