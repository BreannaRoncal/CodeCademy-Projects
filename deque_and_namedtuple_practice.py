"""
Deque and Named Tuple
How to Use:
  from collections import deque and namedtuple
  - Deque: an advanced container which is optimized for appending and popping items from the front and back. 
  - Named Tuple: the namedtuple lets us create an immutable data structure similar to a tuple, but we don’t have to 
    access the stored data using indices. Instead, we can create instances of our namedtuple with named attributes. 
    We can then use the . operator to retrieve data by the attribute names.
    
Goal:
  - The final addition to our clothes store app will be some logic for bundling overstocked items into groups to sell at once. 
  - We would like to split our items by price and then pick three cheaper items and two more expensive items per bundle. 
  - Finally, we are going to promote the bundles which have a value greater than 100 dollars.
"""

from collections import deque, namedtuple

overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

# Write your code below!
split_prices = deque()
for item in overstock_items:
  if item[1] > 20:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)

print(split_prices)

ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

bundles = []
while len(split_prices) >= 5:
  bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(), split_prices.popleft()]
  total_price = sum(i[1] for i in bundle_list)
  bundles.append(ClothesBundle(bundle_list, total_price))

promoted_bundles = []
for b in bundles:
  if b.bundle_price > 100:
    promoted_bundles.append(b)

print(promoted_bundles)
