"""
To further your understanding of functional programming, you will create your own higher-order functions and then use them to process data from a CSV file.

The functions you will create are:
    - count(): will return the frequency of an element in an iterable
    - average(): will return the average of elements in an iterable of numbers
    
    
The count() function will be a special type of filter() function that returns the number of occurrences of an element instead of returning a Boolean value. 
The count() function will accept the following two parameters:
   - predicate: when evaluated to True will allow a counter to increment by one.
   - itr: the collection containing the element of interest.
   
The average() function will compute the arithmetic mean of a collection. You will implement this function recursively to adhere to functional programming principles. 
average() will only accept one parameter: 
   - itr, the collection to be averaged.
"""

import csv
from functools import reduce

def count(predicate, itr):
  count_filter = filter(predicate, itr)
  count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
  return count_reduce   

def average(itr):
  # If itr is not iterable, this will generate an iterator.  
  iterable = iter(itr) 
  return avg_helper(0, iterable, 0)

def avg_helper(curr_count, itr, curr_sum):
  next_num = next(itr, "null")
  if next_num == "null": 
    return curr_sum/curr_count
  curr_count += 1 
  curr_sum += next_num
  return avg_helper(curr_count, itr, curr_sum)

with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  count_belgiums = count(lambda x: x[1] == "Belgium", reader)
  print(count_belgiums)
  csvfile.seek(0)
  avg_portugal = average(map(lambda x: float(x[13]),filter(lambda x: x[1] == "Portugal", reader)))
  print(avg_portugal)

