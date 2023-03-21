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

def naive_solution(heights):
    total_water = 0
    # Traverse every element in the array
    for i in range(1, len(heights) - 1):
        left_bound = 0
        right_bound = 0
    # Find the highest left bound for that index
        for j in range(i + 1):
            left_bound = max(left_bound, heights[j])
    # Find the highest right bound for that index
        for j in range(i, len(heights)):
            right_bound = max(right_bound, heights[j])
    # Take the lower of those two values
    # Subtract the height of that minimum
    # Add the difference to the total amount of water
        total_water += min(left_bound, right_bound) - heights[i]
    return total_water

array = [4, 2, 1, 3, 0, 1, 2]

print(naive_solution(array))

