
from orders import Pizza,Orders

def expensive_pizza(order):
    most_expensive_name = None
    most_expensive_pizza = None
    highest_price = 0
    for nickname in order:
        pizza = order[nickname]
        price = pizza.calc_price()

        if price > highest_price:
            highest_price = price
            most_expensive_name = nickname
            most_expensive_pizza = pizza
    return most_expensive_name,most_expensive_pizza
def show_topping_menu():
    print("Available toppings:")
    for name, price in Pizza.get_topping_menu().items():
        print(f"{name} €{price:.2f}")

def main():
    order = {}

    username = input("please enter your username:")
    order = Orders(username)
    while True:
        answer = input("Would you like to order a pizza? yes enter(Y/y) or any key for no: ").lower()

        if answer != "y":
            break

        nickname = input("Enter a nickname for your pizza:")

        while order.get_pizza(nickname)is not None:
            print("nickname already in use, please enter a different nickname:")
            nickname = input("Enter a different nickname:")
        while True:
            size = input(f"Enter the pizza size ({', '.join(Pizza.get_sizes())}): ").strip()
            if Pizza.is_valid_size(size):
                break
            print("Invalid size")

        show_topping_menu()
        print("Enter 1 topping at a time:")
        print("Press enter to finish")

        toppings = list[str]= []

        while True:
            topping = input("Enter a topping: ").strip().lower()

            if topping == "":
                break

            if not Pizza.is_valid_topping(topping):
                print("Sorry, that isn't on the menu")
            elif topping in toppings:
                print("You already added that topping")
            else:
                toppings.append(topping)

        pizza = Pizza(toppings, size)

        print("Pizza Details")
        print("Nickname:", nickname)
        print("Size:", pizza.get_size())
        print("Toppings:", ", ".join(toppings) if toppings else "none")

        order.add_pizza(nickname,pizza)
        print(f"{pizza.get_size()} pizza added to your order")
    order.display_order()

    nickname, pizza = expensive_pizza(order)
    if pizza is not None:
        print("Most expensive pizza:")
        print("Pizza nickname:", nickname)
        print(f"Price: €{pizza.calc_price():.2f}")




if __name__ == "__main__":
    main()