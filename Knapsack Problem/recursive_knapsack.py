"""
The Knapsack Problem

Imagine that you’re a thief breaking into a house. There are so many valuables
to steal - diamonds, gold, jewelry, and more! But remember, you’re just one
person who can only carry so much. Each item has a weight and value, and your
goal is to maximize the total value of items while remaining within the weight
limit of your knapsack.

Parameters:
    - weight_cap: the total amount of weight you can carry
    - weights: the weights of al the items in an array
    - values: the values of all of the items in an array


Recursive Solution:
    1. weight_cap or i are zero, meaning the knapsack can hold no weight,
       or there are no more items to look at. In either case, we return 0.
    2. The weight of the item we’re looking at exceeds weight_cap,
       in which case we just move on, calling the function on the next item.
    3. If neither of the above are true, that means we have to consider
       whether or not the item we are at (i) should be included in the
       optimal solution.

Runtime: O(2 ^ n)
"""

def recursive_knapsack(weight_cap, weights, values, i):
    # base case
    if weight_cap == 0 or i == 0:
        return 0
    # recursion
    elif weights[i - 1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i - 1)
    else:
        include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)
        exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1)
        return max(include_item, exclude_item)

weight_cap = 5
weights = [1, 3, 5]
values = [250, 300, 500]
i = 2

print(recursive_knapsack(weight_cap, weights, values, i))
