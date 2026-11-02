from solutions.D_using_classes.entities.orders import Pizza

order: dict[str, Pizza] = {}

username = input("Enter your username: ")
order_complete = False

while not order_complete:
    choice = input("Would you like to order a pizza? (Y/y to order, any other key to end)\n")
    if choice.lower() != "y":
        order_complete = True
        continue

    valid_nickname = False
    nickname = ""

    while not valid_nickname:
        nickname = input("Enter new pizza nickname: ")
        if nickname not in order:
            valid_nickname = True
        else:
            print("Nickname already used, please choose another.")

    size = input("What size pizza would you like?\n")

    toppings_complete = False
    toppings = []

    while not toppings_complete:
        topping_choice = input("Would you like to add a topping? (Y/y to add a topping, any other key to end)\n")
        if topping_choice.lower() != "y":
            toppings_complete = True
            continue

        topping = input("Enter topping: ")
        toppings.append(topping)

    if not toppings:
        toppings = ["tomato sauce", "cheese"]

    pizza = Pizza(toppings, size)
    print("Your new pizza's details:")
    pizza.display()

    order[nickname] = pizza

order_total = 0
for pizza in order.values():
    order_total += pizza.calc_price()

print(f"Total price: €{order_total}")