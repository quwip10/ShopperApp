from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
from datetime import date as dt
import sys
import argparse
import logging
logging.basicConfig(level=logging.DEBUG)


def get_item_object(item_number=1):
    '''Prompts user for item name, price, and quantity
        and creates class objects in a list'''

    return (ItemToPurchase(
            item_name=str(input("Enter the item name:\n")),
            item_description=str(input("Enter the item description:\n")),
            item_price=float(input("Enter the item price:\n")),
            item_quantity=int(input("Enter the item quantity:\n"))
            ))


def menu_option(user_input):
    '''checks if valid answer'''
    valid_input = ('a', 'r', 'c', 'i', 'o', 'q')

    if user_input in valid_input:
        return True


def print_menu():
    '''prints a menu and returns user input'''

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

    while not menu_option(user_input):
        user_input = input("Choose an option: ")

    return user_input


def execute_option(user_input, cart):

    if user_input == 'a':
        print("ADD ITEM TO CART")
        cart.add_item(get_item_object())

    elif user_input == 'r':
        print("REMOVE ITEM FROM CART")
        cart.remove_item(input("Enter name of item to remove:\n"))

    elif user_input == 'c':
        print("CHANGE ITEM QUANTITY")
        temp_item = ItemToPurchase(
                item_name=input("Enter the item name:\n"),
                item_quantity=int(input("Enter the new quantity:\n")))
        cart.modify_item(temp_item)

    elif user_input == 'i':
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}".format(
                cart.customer_name, cart.current_date))
        print()
        print("Item Descriptions")
        cart.print_descriptions()

    elif user_input == 'o':
        print("OUTPUT SHOPPING CART")
        cart.print_total()

    return user_input


def import_cart(input_file):
    with open(input_file) as f:
        input_data = f.readlines()

    name_date = input_data.pop(0).strip()
    name = name_date[:name_date.find("'s")]
    date = name_date[name_date.find('-') + 1:].strip()

    user_cart = ShoppingCart(
        customer_name=name,
        current_date=date,
        cart_items=[
            ItemToPurchase(
                item_name=i[:i.find(':')],
                item_description=i[i.find(' '):i.find('x')].strip(),
                item_quantity=int(i[i.find('x')+1:i.find('@')].strip()),
                item_price=int(i[i.find('$')+1:i.find('=')].strip())
                ) for i in input_data
        ])

    return user_cart


# Parse command line arguments
parser = argparse.ArgumentParser()

parser.add_argument(
    '--interactive',
    action='store_true',
    help='Opens program in interactive mode')
parser.add_argument(
    '-i', '--input',
    default='',
    type=str,
    metavar='input file',
    help='input filename'
)
parser.add_argument(
    '-o', '--output',
    default="cart_export.txt",
    type=str,
    metavar='output file',
    help='output filename'
)
args = parser.parse_args()

logging.info("Input file: {} Output file: {}".format(args.input, args.output))
logging.info("Interactive mode={}".format(args.interactive))

# Main
# Created 9-24-19
# Last updated 9-24-19
# Aheidenreich

if __name__ == "__main__" and args.interactive:

    # School required code

    name = input("Enter customer's name (First Last): ")
    print("Enter today's date (YYYY-MM-DD)")
    date = input("Default is {}: ".format(dt.today()))

    if not date.strip():
        logging.info("No date entered. Using today's date.")
        date = dt.today()

    # Create new Shopping cart object from input
    user_cart = ShoppingCart(
            customer_name=name,
            current_date=date)

    # Print input back to screen
    print("\nCustomer name: {}".format(name))
    print("Today's date: {}".format(date))

    while execute_option(print_menu(), user_cart) != 'q':
        continue

    if input("Do you want to save your cart? ").lower()[0] == 'y':
        user_cart.export_cart(input("Enter a filename(Default is {}): "
                                    .format(args.output or "cart_export.txt"))
                              or args.output
                              or "cart_export.txt")

elif args.input:
    user_cart = import_cart(args.input)
    user_cart.export_cart(args.output or "cart_export.txt")

else:
    try:
        raise OSError
    except OSError:
        print("Must be run in either interactive mode with --interactive\n"
              "or with -i INPUT FILE\n"
              "See -h or --help for more information.")
