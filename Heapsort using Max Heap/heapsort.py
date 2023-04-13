"""
Heapsort in Python

Let’s go over what we learned about heapsort:

  1. A heapsort algorithm uses the heap data structure to organize data.
  2. The first step to implement heapsort is to place the data inside a heap.
  3. While the heap has more than one element, extract the largest value in the heap by swapping it with the right-most child and then removing it.
  4. After we swap the root value and the last value, we must restructure the heap until every parent has a larger value than their children again.
  
"""

from max_heap import MaxHeap 

def heapsort(lst):
  sort = []
  max_heap = MaxHeap()
  for idx in lst:
    max_heap.add(idx)
  while max_heap.count > 0:
    max_value = max_heap.retrieve_max()
    sort.insert(0, max_value)
  return sort

my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print(sorted_list)
