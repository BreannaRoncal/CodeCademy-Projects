"""
Practice Unit Testing for surfshop.py

  - Define a test method that calls this function with an argument of 1 and checks that 'Successfully added 1 surfboard to cart!' is returned.
  - Create another test method which calls ShoppingCart.add_surfboards(), but this time, passes an argument of 2. 
    It should test that the return value is 'Successfully added 2 surfboards to cart!'
  - Create a test to check that a surfshop.TooManyBoardsError (a custom exception) is raised when ShoppingCart.add_surfboards() is called with an argument of 5.
  - Create a test that calls ShoppingCart.apply_locals_discount() and then checks that ShoppingCart.locals_discount is True.
"""

# Write your code below:
import surfshop
import unittest
import datetime

class TestSurfshop(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboard(self):
    message = self.cart.add_surfboards(quantity=1)
    self.assertEqual(message, f'Successfully added 1 surfboard to cart!')
    

  # Parameterize the test you wrote in task 4 so that it runs 3 times, passing 2, 3, and 4 as the arguments to surfshop.add_surfboards(). 
  # This allows us to easily test a single function with a variety of inputs. 
  def test_add_surfboards(self):
    for num in range(2, 5):
      with self.subTest():
        message = self.cart.add_surfboards(num)
        print(message)
        self.assertEqual(message, f'Successfully added {num} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()


        
  # Sam, the owner of Sam’s Surf Shop, has just informed us that the shop is heading into the off season and business has slowed down. 
  # The store’s shopping cart no longer needs to enforce the 4 surfboards per customer rule - at least until business picks up again.
  # Go back and modify the test you wrote in task 5 which checks for a surfshop.TooManySurfboardsError so that it is skipped.
  @unittest.skip
  def test_TooManyBoardsError(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
    
  # The @unittest.expectedFailure decorator can mark tests as expected to fail.
  # @unittest.expectedFailure
  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

    
  # If you want to challenge yourself even further, take a look at the ShoppingCart.set_checkout_date() function. 
  # This function takes a datetime.datetime object as an argument and raises a surfshop.CheckoutDateError if the date is not in the future.
  def test_invalid_checkout_date(self):
    date = datetime.datetime.now()
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)


    
unittest.main()
