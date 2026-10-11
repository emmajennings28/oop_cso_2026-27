class Pizza:
    size_and_price = {
        "small" :10,
        "medium" :12,
        "large" : 14,
        "x_large" :16
    }

    toppings = {}

    def __init__(self,toppings, size="Medium"):
        self.toppings = toppings

        if size in self.size_and_price:
            self.__size = size
        else:
            self.__size = "Medium"

    def display(self):
        if self.toppings == 0:
            print(self.__size + "pizza with no toppings")
        else:
            print(self.__size + "pizza with" + ",".join(self.toppings)+"toppings")

    def get_size(self):
        return self.__size
