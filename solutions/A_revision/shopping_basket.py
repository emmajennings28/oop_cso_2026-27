# Answer to C1:
def calc_item_price(item_dict):
    # Calculate the price of this item: item price * quantity in basket
    return item_dict["price"] * item_dict["quantity"]

# Calculate the total price of the basket
def calc_basket_price(basket_list):
    total = 0
    # Loop through each item in the basket
    for item in basket_list:
        # Add its price to the basket's total
        total += calc_item_price(item)

    return total

# Answer to C2:
def print_receipt(basket_list):
    print("-" * 45)
    print("\tThank you for shopping at our store")
    for item in basket_list:
        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]

        subtotal = price * quantity
        # fstring formatting codes help with alignment
        # < left aligns to X characters
        # > right aligns to X characters
        # .2f specifies it should display numbers to 2 decimal places
        # \t (not specifically an fstring code!) inserts a tab character
        print(f"{name:<20} {quantity:>2} x €{price:>5.2f} \t€{subtotal:>4.2f}")

# Answer to C3:
def find_item(basket_list, item_name):
    for item in basket_list:
        # Use .lower() to neutralise the case
        # This way the case of the text doesn't matter!
        if item["name"].lower() == item_name.lower():
            return item

    # Where there's no match, return None as a clear indication of this
    # None is more useful than text - text is too variable, too many possibilities!
    return None

# Answer to C4:
def change_quantity(basket_list, item_name, new_quantity):
    # If the quantity is illegal, reject it and return False
    if new_quantity < 0:
        print("Cannot have a negative quantity.")
        return False

    # Use existing function to find the matching item
    item = find_item(basket_list, item_name)

    # If we find a match, update the quantity and return True
    if item is not None:
        item["quantity"] = new_quantity
        return True
    else:
        return False

# Answer to C5:
def calc_total(basket_list):
    basket_total = calc_basket_price(basket_list)
    if basket_total >= 50:
        discount = basket_total * .1
        basket_total = basket_total - discount

    return basket_total


if __name__ == "__main__":
    basket = [
        {"name": "Yogurt", "price": 1.79, "quantity": 4},
        {"name": "Bread", "price": 1.80, "quantity": 1},
        {"name": "Milk", "price": 1.59, "quantity": 2}
    ]
    # Answer to C1:
    print(f"The total price of this basket is: {calc_basket_price(basket)}")

    print("-"*20)

    # Testing answer for C2:
    print_receipt(basket)

    # Testing answer for C3:
    print("-" * 20)
    print("Searching for 'Yogurt'")
    yogurt = find_item(basket, "yogurt")
    print(f"Search result for 'yogurt': {yogurt}")

    print()

    print("Searching for 'Banana'")
    banana = find_item(basket, "banana")
    print(f"Search result for 'banana' (No match should be found): {banana}")

    # Testing answer for C4:
    print("-" * 20)
    print("Updating quantity for 'yogurt' - increasing to 5")
    updated = change_quantity(basket, "Yogurt", 5)
    if updated:
        print("'Yogurt' quantity updated!")
        print(yogurt)
    else:
        print("Could not update quantity for 'Yogurt'")

    # Testing answer for C5:
    print("-" * 20)
    print(f"Total price for normal basket: €{calc_total(basket)}")

    expensive_basket = [
        {"name": "Cheerios", "price": 7.80, "quantity": 3},
        {"name": "Coke Zero", "price": 12.00, "quantity": 4},
    ]
    print(f"Total price for expensive basket: €{calc_total(expensive_basket)}")