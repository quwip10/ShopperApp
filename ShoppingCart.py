# Shopping Cart Class


class ShoppingCart():
    '''Customer shopping cart class'''

    def __init__(
            self,
            customer_name="none",
            current_date="January 1, 2016",
            cart_items=[]):

        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def __iter__(self):
        # FIXME is this necessary?
        return self.cart_items

    def __contains__(self, item):
        for i in self.cart_items:
            if i == item.item_name:
                return True
        return False

    def add_item(self, item):
        '''Adds an item to cart_items list. Does not return anything'''

        self.cart_items.append(item)

    def remove_item(self, item_str):
        '''Removes item from cart_items list by name.
            Does not return anything'''

        for i in self.cart_items:
            if i.item_name == item_str:
                return self.cart_items.remove(i)

        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        '''Modifies an item's description, price, and/or quantity.
            Does not return anything.
            If item can be found by name in cart,
            check if parameter has default values
            for description, price and quantity. If not, modify item in cart.
            If item cannot be found by name in cart, output error'''

        for i in self.cart_items:
            if i.item_name == item.item_name:
                if (item.item_price != i.item_price)\
                        and (item.item_price != 0):
                    i.item_price = item.item_price
                if (item.item_quantity != i.item_quantity)\
                        and (item.item_quantity != 0):
                    i.item_quantity = item.item_quantity
                if (item.item_description != i.item_description)\
                        and (item.item_description != "none"):
                    i.item_description = item.item_description
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        '''Returns quantity of all items in cart'''

        num_items = 0

        for i in self.cart_items:
            num_items += i.item_quantity

        return num_items

    def get_cost_of_cart(self):
        '''Determines and returns total cost of items in cart'''

        return sum([i._calc_total_cost() for i in self.cart_items])

    def print_total(self):
        '''Output total of objects in cart or empty'''

        print("{}'s Shopping Cart - {}".format(
            self.customer_name, self.current_date))
        print("Number of Items: {}".format(self.get_num_items_in_cart()))
        print()
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            [print(i.print_item_cost()) for i in self.cart_items]
        print()
        print("Total: ${:.0f}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        '''Output each item's descriptions'''
        [print(i.print_item_description()) for i in self.cart_items]

    def export_cart(self, filename="cart_export.txt"):
        '''take input filename and export cart to file'''

        with open(filename, mode='w') as f:
            f.write("{}'s Shopping Cart - {}\n".format(
            self.customer_name, self.current_date))

            [f.write(i.print_all() + "\n") for i in self.cart_items]