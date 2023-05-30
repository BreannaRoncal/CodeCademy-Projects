"""
In this exercise, we will see how we can process the data that is stored in a CSV file.
When working with a file that contains a large amount of data, generating every possible record 
using tuple() is inefficient. Recall from the previous exercise that map() returns an iterator that 
we can use to bring in data. We can apply the higher-order functions to this iterator to process 
the data and only bring in the relevant set of records.

   1. Create a tuple called trees and populate it with data of trees that have a height greater than 75.
   2. Create a variable called widest and store in it the record of the widest tree in trees. 
      You may want to print the answer to see which tree is the widest!
"""

import csv
from collections import namedtuple
from functools import reduce

tree = namedtuple("tree", ["index", "width", "height", "volume"]) 

with open('trees.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  next(reader)
  mapper = map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)
  
  # Checkpoint 1 code goes here.
  t = filter(lambda x: x[2] > 75, mapper)
  trees = tuple(t)

  # Checkpoint 2 code goes here.
  widest = reduce(lambda x, y: x if x.width > y.width else y, trees)
  print(widest)
