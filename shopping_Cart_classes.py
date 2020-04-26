class ShoppingCart(object):
    def __init__(self,customer_name):
        self.customer_name = customer_name
        self.customer_cart = {}
    def add_cart(self,name,product,price):
        self.product = product
        self.price = price
        if name == self.customer_name:
            print("Valid user.")
            if not product in self.customer_cart:
                self.customer_cart[product] = price
                print("Product was added to cart.")
            else:
                print("Product already in cart")
        else:
            print("Invalid User.")
    def delete_cart(self,product):
        if product in self.customer_cart:
            del self.customer_cart[product]
            print("Product deleted from cart.")
        else:
            print("Product not in cart.")
    def show_cart(self):
        print("Here is your current cart:\n {}".format(self.customer_cart))
        print("Total cost : {}".format(sum(self.customer_cart.values())))
        

customer = ShoppingCart("Fabian")
customer.add_cart("Fabian","Fish",27)
customer.add_cart("Fabian","Beef",13)
customer.add_cart("Robber","Skittles",5)
customer.show_cart()

