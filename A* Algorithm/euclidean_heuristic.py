"""
Modify Dijkstra's Algorithm to an A* Algorithm with the Euclidean Heuristic:
    - Works in a non-grid system, where the shortest distance is closer to a direct diagonal between start and target 
    - Uses Pythagorean theorem to get the estimated distance:
        return the squareroot of x_distance^2 + y_distance^2
"""

from math import inf, sqrt
from heapq import heappop, heappush
from euclidean_graph import euclidean_graph, bengaluru, jaipur

# Change heuristic() below:
def heuristic(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return sqrt(x_distance ** 2 + y_distance ** 2)

def a_star(graph, start, target):
  print("Starting A* algorithm!")
  count = 0
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]
  while vertices_to_explore and paths_and_distances[target][0] == inf:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight + heuristic(neighbor, target)
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
  
  return paths_and_distances[target][1]

# Call a_star() on euclidean_graph to find the best route
# from jaipur to bengaluru:
a_star(euclidean_graph, jaipur, bengaluru)