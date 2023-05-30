"""
A CSV file often contains millions of lines of data. Importing the entire contents of a CSV file is impractical as this would occupy too much 
RAM resulting in poor program performance. to avoid importing all the data at once, reader is an iterator object that maintains a pointer to 
the file and iterates through the data when next(reader) is called.

1. We create a namedtuple to represent each record
2. To work with a csv file, we must first open it and create a reader object (an iterator) that will read the file
3. We use the map() function to read in a line of data and store it in a tuple. Incoming data arrives as a list of strings regardless of 
   their intended type; therefore we must cast each element to convert it to the proper type. The order of the data is dictated by the first line in a CSV file.
"""

import csv
from collections import namedtuple
from functools import reduce

# Code for Checkpoint 1 goes here.
tree = namedtuple("tree", ["index", "width", "height", "volume"])

with open('trees.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  next(reader) # Skip the first line in trees.csv that contains the data lablels.
  # Code for Checkpoint 2 goes here.
  mapper = map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)
  
  trees = tuple(mapper)
  print(trees)
