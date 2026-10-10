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
            

