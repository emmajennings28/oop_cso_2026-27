from exercise_materials.exercises.Classes.orders import Pizza
from orders import Pizza

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
    size = size.lower()

    toppings = []
    print("Enter 1 topping at a time:")
    print("Press enter to finish")

    while True:
        topping = input("Enter a topping:").strip()

        if topping == "":
            break

        toppings.append(topping)

    if len(toppings) == 0:
        toppings = ["tomato sauce","cheese"]

    pizza = Pizza(toppings, size)

    print("Pizza Details")
    print("Nickname:",nickname)
    print("Size:", size)
    print("Toppings:",",".join(toppings))

    order[nickname]=pizza
    print("Pizza added to your order")

print("Order summary for",username)
if len(order) == 0:
    print("You havent ordered any pizzas")
else:
    for nickname, pizza in order.items():
        print("Pizza nickname:",nickname)
        pizza.display()