class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity


class Cart:
    def __init__(self):
        self.products = []  # List of Product instances
        self.total_price = 0.0

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        for i in range(len(self.products)):
            if self.products[i].product_id == product.product_id:  # Compare using product_id
                del self.products[i]
                break  # Exit once the product is found and removed

    def calculate_total(self):
        total_price = 0
        for product in self.products:
            total_price += product.price  # Sum the prices of all products
        print(f"Total cart price: {total_price}")


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = Cart()

    def view_cart(self):
        cart_items = []
        if self.cart.products:  # Check if there are products in the cart
            for product in self.cart.products:
                cart_items.append(product.name)  # Append product name (or any other information)
        print("Cart items are:", cart_items)


class Order:
    def __init__(self, order_id, customer, order_date, order_items, order_status):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.order_items = order_items
        self.order_status = order_status

    def place_order(self):
        if self.order_items and self.customer.cart.products:
            print("Order placed successfully")
        else:
            print("Order could not be placed. Cart is empty.")


# Testing the system

product1 = Product(1, "Mysoorsandal_soap", 85, 1)
product2 = Product(2, "Headandshoulders_shampoo", 100, 2)

customer = Customer(11, "Ramesh")
order1 = Order(1, customer, "08-03-2025", customer.cart.products, "order_placed_successfully")

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)

customer.view_cart()

# Place order after adding products to cart
order1.place_order()

cart.calculate_total()  # Calculate the total price of products in the cart
