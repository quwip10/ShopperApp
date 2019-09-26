from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase

my_item1 = ItemToPurchase()
my_item2 = ItemToPurchase("Thing", 5, 10, "A thingamabob")

my_cart = ShoppingCart(
    customer_name="Bob",
    current_date="Today",
    cart_items=[my_item1, my_item2])

if my_item2 in my_cart:
    print("Heckin Cool")
