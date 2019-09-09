
# aheidenreich
# Lab 11.11

# Imports
import sys


# Global Variables
object_list = []


# Classes
class ItemToPurchase():
    '''Shopping cart item takes item_name, item_price, and item_quantity'''

    def __init__(
            self,
            item_name="none",
            item_price=0,
            item_quantity=0):
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

    '''object_list = [get_object(item_count) for item_count in range(num_objects)]'''

    # School required code
    item1 = get_object(0)
    print()
    item2 = get_object(1)
    print()

    print("TOTAL COST")
    print(item1.print_item_cost())
    print(item2.print_item_cost())

    print()
    print("Total: ${:.0f}".format(item1 + item2))
