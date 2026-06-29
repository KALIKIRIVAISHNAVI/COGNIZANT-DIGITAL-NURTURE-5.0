def display_cart():
    cart = [100, 250, 75]

    if not cart:
        print("Cart is empty")
        return

    print("Cart Contents:")
    for item in cart:
        print(item)

display_cart()