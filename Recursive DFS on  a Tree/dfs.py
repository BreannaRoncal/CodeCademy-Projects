"""
To recap this lesson, you gained practice with:

  1. Using the TreeNode class to store a tree data structure.
  2. Implementing a recursive method that searches for a path to a node with a specified value using the recursive paradigm often called “divide and conquer.”
  3. Default function arguments in Python.
  4. Tuples, which are immutable lists, can be a convenient choice over lists for recursive methods like this.
  5. Python will implicitly return None from functions that terminate without reaching a return statement, but it can be a good practice to explicitly 
     return None when other components expect None to be returned sometimes.
     
"""

from TreeNode import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)

def dfs(root, target, path=()):
  path = path + (root,)

  if root.value == target:
    return path

  for child in root.children:
    path_found = dfs(child, target, path)

    if path_found is not None:
      return path_found

  return None
        
path = dfs(sample_root_node, "F")
print(path)
