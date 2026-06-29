class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def calculate_total(self):
        return sum(item.total() for item in self.items)

    def print_receipt(self):
        print("\n--- Receipt ---")
        for item in self.items:
            print(item.name, item.price, "x", item.quantity, "=", item.total())

        total = self.calculate_total()
        gst = total * 0.18
        final = total + gst

        print("\nSubtotal:", total)
        print("GST (18%):", gst)
        print("Final Total:", final)


# Example usage
cart = ShoppingCart()

cart.add_item(CartItem("Book", 200, 2))
cart.add_item(CartItem("Pen", 20, 5))
cart.add_item(CartItem("Bag", 500, 1))

cart.remove_item("Pen")
cart.print_receipt()