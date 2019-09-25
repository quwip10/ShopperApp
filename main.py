import sys
from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
from datetime import date as dt

def get_item_object(item_number=1):
    '''Prompts user for item name, price, and quantity
        and creates class objects in a list'''

    # FIXME remove below line?
    # print("Item {}".format(item_number + 1))
    return (ItemToPurchase(
            item_name=str(input("Enter the item name:\n")),
            item_description=str(input("Enter the item description:\n")),
            item_price=float(input("Enter the item price:\n")),
            item_quantity=int(input("Enter the item quantity:\n"))
            ))


def print_menu(cart):
    '''prints a menu and edits shopping cart item'''

    user_input = None
    valid_choices = ('a', 'r', 'c', 'i', 'o', 'q')

    print('''
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
''')

    while user_input not in valid_choices:
        user_input = input("Choose an option:\n")

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


# Main
# Created 9-24-19
# Last updated 9-24-19
# Aheidenreich

if __name__ == "__main__":

    # School required code

    name = input("Enter customer's name (First Last): ")
    print("Enter today's date (YYYY-MM-DD)")
    date = input("Default is {}: ".format(dt.today()))
    if not date.strip():
        date = dt.today()

    # Create new Shopping cart object from input
    user_cart = ShoppingCart(
            customer_name=name,
            current_date=date)

    # Print input back to screen
    print("\nCustomer name: {}".format(name))
    print("Today's date: {}".format(date))

    user_selection = "none"
    while user_selection != 'q':
        user_selection = print_menu(user_cart)

