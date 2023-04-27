"""
Sam's Surf Shop

You’ve been hired to create a handful of tests for the shopping cart software at the surf shop. 
Once that is done, you’ll implement some improvements for these tests using more advanced unit testing features 
(skipping, parameterization, and expected failures). Finally, you’ll have the opportunity to fix bugs that were exposed by your tests.

The shopping cart software for Sam’s Surf Shop lives inside of the file called surfshop.py. 
Look over the files and familiarize yourself with their contents. 
Most of our work will take place in tests.py.

"""

import datetime

class TooManyBoardsError(Exception):
    "Cart cannot have more than 4 surfboards in it!"

class CheckoutDateError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.num_surfboards = 0
        self.checkout_date = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self.num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    def set_checkout_date(self, date):
        if date <= datetime.datetime.now():
            raise CheckoutDateError
        else:
            self.checkout_date = date

    def apply_locals_discount(self):
        self.locals_discount = True
