
from orders import Pizza

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

def main():
    order = {}

    username = input("please enter your username:")

    while True:
        answer = input("Would you like to order a pizza? yes enter(Y/y) or any key for no: ").lower()

        if answer != "y":
            break

        nickname = input("Enter a nickname for your pizza:")

        while nickname in order:
            print("nickname already in use, please enter a different nickname:")
            nickname = input("Enter a different nickname:")

        size = input("Enter the pizza size:")
        if size.lower() not in ["Small","Medium","Large","X_large"]:
            new_pizza = Pizza.new_size()
            return new_pizza
        else:
            return False

        print("Enter 1 topping at a time:")
        print("Press enter to finish")

        while True:
            topping = input("Enter a topping:").strip()

            if topping == "":
                break

            toppings.append(topping)

        if len(toppings) == 0:
            toppings = ["tomato sauce","cheese"]

        pizza = Pizza(topping, size)

        print("Pizza Details")
        print("Nickname:",nickname)
        print("Size:", size)
        print("Toppings:",",".join(toppings))

        order[nickname]=pizza
        print(f"{size} pizza added to your order")

    print("Order summary for",username)
    total = 0
    for nickname in order:
        pizza = order[nickname]
        price = pizza.calc_price()
        print(f"{nickname}€{price}")
        total = total+price
    if len(order) == 0:
        print("You haven't ordered any pizzas")
    else:
        nickname, pizza = expensive_pizza(order)
        print("Most expensive pizza:")
        print("Pizza nickname:",nickname)
        print(f"Price:€ {pizza.calc_price():.2f}")

    print(f"{username}'s total bill is € {total}")
if __name__ == "__main__":
    main()
