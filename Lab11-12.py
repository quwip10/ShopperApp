
# aheidenreich
# Lab 11.11

# Imports
import sys


# Global Variables
object_list = []


# Classes
class ItemToPurchase():
    '''Shopping cart item takes
        item_name, item_price, item_quantity, and item_description'''

    def __init__(
            self,
            item_name="none",
            item_price=0,
            item_quantity=0,
            item_description=None):
        '''initializes a class with default values of zero'''

        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        '''prints total cost of x quantity of items'''

        return ("{} {} @ ${:.0f} = ${:.0f}".format(
                self.item_name,
                self.item_quantity,
                self.item_price,
                self._calc_total_cost()))

    def print_item_description(self):
        '''prints description of item'''

        return ("{}: {} ".format(
                self.item_name,
                self.item_description))

    def _calc_total_cost(self):
        '''calculates the total cost of x items'''

        return (self.item_price * self.item_quantity)

    def __str__(self):
        '''overloads string statement to print the attributes'''

        return ("Item name: {}\nItem price: ${:.2f}\nItem quantity: {}".format(
                self.item_name,
                self.item_price,
                self.item_quantity))

    def __add__(self, other):
        '''allows adding of objects to return total cost'''

        if isinstance(other, ItemToPurchase):
            return (self._calc_total_cost() + other._calc_total_cost())
        elif isinstance(other, float) or isinstance(other, int):
            return (self._calc_total_cost() + other)
        else:
            print("Unsupported type: {} {}".format(other, type(other)))


class ShoppingCart():
    '''Customer shopping cart class'''

    def __init__(
            self,
            customer_name=None,
            current_date="January 1, 2016",
            cart_items=[]):

        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, item_to_add):
        '''Adds an item to cart_items list. Does not return anything'''

        self.cart_items.append(item)

    def remove_item(self, item_name):
        '''Removes item form cart_items list by name.
            Does not return anything'''

        if item in self.cart_items:
            self.cart_items.remove(item)
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        '''Modifies an item's description, price, and/or quantity.
            Does not return anything.
            If item can be found by name in cart,
            check if parameter has default values
            for description, price and quantity. If not, modify item in cart.
            If item cannot be found by name in cart, output error'''

        if item_name in self.cart_items:
            self.cart_items.remove(item_name)
        else:
            print("Item not found in cart. Nothing modified.")
        pass

    def get_num_items_in_cart(self):
        '''Returns quantity of all items in cart'''

       return len(self.cart_items) 

    def get_cost_of_cart(self):
        '''Determines and returns total cost of items in cart'''

        pass

    def print_total(self):
        '''Return? Output? total of objects in cart or empty'''

        pass

    def print_descriptions():
        '''Output each item's descriptions'''

        pass


# Functions
def get_object(item_number=1):
    '''Prompts user for item name, price, and quantity
        and creates class objects in a list'''

    print("Item {}".format(item_number + 1))
    return (ItemToPurchase(
            str(input("Enter the item name:\n")),
            float(input("Enter the item price:\n")),
            int(input("Enter the item quantity:\n"))
            ))


# Main
if __name__ == "__main__":
    '''Prompts user for item name, price, and quantity
        and creates class objects in a list'''

    num_objects = 2

    # check if command line argument to input quantity of items
    if len(sys.argv) > 1:
        # check if isdigit and only one arg
        if len(sys.argv) > 2 or not sys.argv[1].isdigit():
            print("Usage: python3 Lab11-11 item_quantity")
            sys.exit(1)
        else:
            num_objects = int(sys.argv[1])

    '''object_list = [get_object(item_count)
        for item_count in range(num_objects)]'''

    # School required code

