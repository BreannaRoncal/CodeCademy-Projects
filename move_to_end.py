"""
Move items to the end of the list

As you know by now, a List in Python is used to store multiple items in a single variable. Unfortunately, the order of items might not always be the one we want. 
The following problem represents a scenario where a list needs to be reorganized.

Alex is a gemstone collector who recently placed an order for an assortment of ambers, jades, pearls, and sapphires. When he opened the delivery package, 
Alex found that his list of gemstones was mixed up.

Alex is particularly fond of a certain type of gemstone and wants to move them to the end of his gallery display. 
Let’s design a recursive algorithm to help Alex set up his gallery:

  1. Define a function that takes in two arguments: a list and a string. The string will represent the value we are looking for in the list.
  2. Create a result variable and assign it to an empty list []. This variable will store the final result.
  3. Address the base case: if the given list is empty, return an empty list.
  4. The recursive step can go either of two ways:
      a) If the first item in the list matches the value we are looking for, set the value of result to a recursive call in which the first argument is 
         our list of values minus the first element and the second argument is the value we are looking for. Then append the first item of the list to result.
      b)Else, append the first item of the list to result. Then set the value of result to a recursive call in which the first argument is our list of 
        values minus the first element and the second argument is the value we are looking for.
  5. Finally, return result.
  
"""

# define move_to_end() here
def move_to_end(lst, val):
  result = []
  if len(lst) == 0:
    return result
  curr_val = lst[0]

  if curr_val == val:
    result += move_to_end(lst[1:], val)
    result.append(curr_val)
    return result
  else:
    result.append(curr_val)
    result += move_to_end(lst[1:], val)
    return result

 

# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))
