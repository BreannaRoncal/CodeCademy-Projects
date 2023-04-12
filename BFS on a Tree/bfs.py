"""
Let’s go over the steps taken to create a breadth-first search function:

  1. Before starting the search, define the tree’s root node as well as a value to search for.
  2. Initialize a frontier queue, which holds a path for each node to search
  3. Loop through the frontier queue to check if the node value matches the value we are searching for.
  4. Continue the search by adding child nodes to the frontier until the goal has been found, or the tree has been completely searched.
  
"""


from collections import deque

# Breadth-first search function
def bfs(root_node, goal_value):

  # initialize frontier queue
  path_queue = deque()

  # add root path to the frontier
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  # search loop that continues as long as
  # there are paths in the frontier
  while path_queue:
    # get the next path and node 
    # then output node value
    current_path = path_queue.pop()
    current_node = current_path[-1]
    print(f"Searching node with value: {current_node.value}")

    # check if the goal node is found
    if current_node.value == goal_value:
      return current_path

    # add paths to children to the  frontier
    for child in current_node.children:
      new_path = current_path[:]
      new_path.append(child)
      path_queue.appendleft(new_path)

  # return an empty path if goal not found
  return None
