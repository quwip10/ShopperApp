# ItemToPurchase Class


class ItemToPurchase():
    '''Shopping cart item takes
        item_name, item_price, item_quantity, and item_description'''

    def __init__(
            self,
            item_name="none",
            item_price=0.0,
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

        return ("{}: {}".format(
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