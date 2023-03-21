"""
Capturing Rainwater
Imagine a very heavy rainstorm over a highway that has many potholes and cracks.
The rainwater will collect in the empty spaces in the road, creating puddles.
Each puddle can only be as high as the road around it, as any excess water
will just flow away.

The capturing rainwater problem asks you to calculate how much rainwater would
be trapped in the empty spaces in a histogram (a chart which consists of a
series of bars).

This can be represented in Python as an array filled with the values
[4, 2, 1, 3, 0, 1, 2].
Imagine that rainwater has fallen over the histogram and collected between
the bars.

Like with the road, the amount of water that can be captured at any given
space cannot be higher than the bounds around it. To solve the problem,
we need to write a function that will take in an array of integers and
calculate the total water captured. 
"""


"""
pseudo code:

total_water = 0
left_pointer = 0
right_pointer = heights.length - 1
left_bound = 0
right_bound = 0

while left_pointer < right_pointer:
    if the height at the left_pointer <= the height at the right_pointer:
        - update the left_bound to be the greater value between the current left_bound and the height at the left_pointer
        - increment total_water to be the difference bewteen left_bound and the height at left_pointer
        - move left_pointer forward by one
    else:
        - update the right_bound to be the greater value bewteen the current right_bound and the height at right_pointer
        - increment total_water to be the difference between right_bound and the height at right_pointer
        - move right_pointer back by one
    
return total_water
"""

def optimized_solution(heights):

  total_water = 0
  left_pointer = 0
  right_pointer = len(heights) - 1
  left_bound = 0
  right_bound = 0

  # Write your code here
  while left_pointer < right_pointer:
    left_bound = max(left_bound, heights[left_pointer])
    right_bound = max(right_bound, heights[right_pointer])
    if left_bound <= right_bound:
      total_water += left_bound - heights[left_pointer]
      left_pointer += 1
    else:
      total_water += right_bound - heights[right_pointer]
      right_pointer -= 1

  return total_water


test_array = [4, 2, 1, 3, 0, 1, 2]
print(optimized_solution(test_array))
# Print 6
