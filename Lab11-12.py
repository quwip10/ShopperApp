
# aheidenreich
# Lab 11.11

# Imports
import sys


# Global Variables
object_list = []


# Classes
class Shopper():
    '''shopper object with attributes'''

    def __init__(name="none", date="none"):
        '''initialize Shopper'''

        self.name = name
        self.date = date

class ItemToPurchase():
    '''Shopping cart item takes
        item_name, item_price, item_quantity, and item_description'''

    def __init__(
            self,
            item_name="none",
            item_price=0,
            item_quantity=0,
            item_description="none"):
        '''initializes a class with default values of zero'''

        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

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
        # FIXME debug statment below
        print("debugged")
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

        if item in self.cart_items:
            #FIXME fill this out
            pass
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        '''Returns quantity of all items in cart'''

        return (len(self.cart_items))

    def get_cost_of_cart(self):
        '''Determines and returns total cost of items in cart'''

        return sum([i._calc_total_cost() for i in self.cart_items])

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

#    print("Item {}".format(item_number + 1))
    return (ItemToPurchase(
            str(input("Enter the item name:\n")),
            str(input("Enter the item description:\n")),
            float(input("Enter the item price:\n")),
            int(input("Enter the item quantity:\n"))
            ))


def print_menu(cart):
    '''prints a menu and edits shopping cart item'''

    user_input = None

    print('''
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
''')

    while user_input != 'q':
        user_input = input("Choose an option:\n")

        if user_input == 'a':
            print("ADD ITEM TO CART")
            cart.add_item(get_object())

        elif user_input == 'r':
            print("REMOVE ITEM FROM CART")
            cart.remove_item(input("Enter name of item to remove:\n"))

        elif user_input == 'c':
            print("CHANGE ITEM QUANTITY")
            temp_item = ItemToPurchase(
                    item_name=input("Enter the item name:\n"),
                    item_quantity=int(input("Enter the new quantity:\n")) )
            cart.modify_item(temp_item)

        elif user_input == 'i':
            pass
        elif user_input == 'o':
            pass


# Main
if __name__ == "__main__":

    # School required code

    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")

    # Create new Shopping cart object from input
    user_cart = ShoppingCart(
            customer_name=name,
            current_date=date)
    
    # Print input back to screen
    print("\nCustomer name: {}".format(name))
    print("Today's date: {}".format(date))

    print_menu(user_cart)
