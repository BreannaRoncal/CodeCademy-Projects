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


Dynamic Programming Solution:
    - Use memoization to store information instead of making duplicate calls
        - store this information in a two-dimensional array that has a
          row for every item and weight_cap + 1 number of columns where each
          element in the 2D array (matrix) represents a subproblem.
          The element at the bottom right will be the optimal solution.
        - rows represent items we've seen
        - columns represent how much weight the knapsack can hold

    pseudocode:

    matrix = 2D array with rows equal to number of items and empty columns
    for every number of items you can carry (index):
        fill matrix[index] with an array of length weight_cap + 1
        for every weight < weight_cap(weight):
            if index or weight == 0:
                set element at [index][weight] to 0
            else if the weight of element at index - 1 <= weight:
                find possible values of including and excluding the item
                set element at [index][weight] to max of those values
            else:
                set element at [index][weight] to element one above
    return element at bottom right of matrix

"""


def dynamic_programming_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1
  cols = weight_cap + 1
  # Set up 2D array
  matrix = [ [] for x in range(rows) ]

  # Iterate through every row
  for index in range(rows):
    # Initialize columns for this row
    matrix[index] = [ -1 for y in range(cols) ]

    # Iterate through every column
    for weight in range(cols):
      # Write your code here
      if index == 0 or weight == 0:
        matrix[index][weight] = 0
      # If weight at previous row is less than or equal to current weight
      elif weights[index - 1] <= weight:
        # Calculate item to include
        include_item = values[index - 1] + matrix[index - 1][weight - weights[index - 1]]

        # Calculate item to exclude
        exclude_item = matrix[index - 1][weight]
        matrix[index][weight] = max(include_item, exclude_item)
      else:
        # Calculate the value of current cell
        matrix[index][weight] = matrix[index - 1][weight]

  # Return the value of the bottom right of matrix
  return matrix[rows-1][weight_cap]

# Use this to test your function:
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(dynamic_programming_knapsack(weight_cap, weights, values))

