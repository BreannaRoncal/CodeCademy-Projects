"""
We may find ourselves in situations where we are working with JSON Data. 
The JSON format is the preferred way to structure data such that it may be transmitted over the internet. 
An API call usually responds with data formatted in JSON. We can process JSON data using the higher-order functions we have been working with.

However, unlike a CSV file, we cannot use an iterator when we read data from a JSON file. The file’s entire contents are read and stored 
in a Python dictionary. If a JSON object contains another JSON object, the dictionary will contain another dictionary. Unfortunately, 
the json library in Python does not provide a method to produce an iterator that we can use to read data similar to a CSV; we will have to work with the dict type.

   1. To work with the JSON file, we must first be open it and read it as we did for a CSV file
   2. The data formatted this way is hard to read and susceptible to errors when using it. 
      It would be better to use map() to store this data as a namedtuple
   3. The cities iterable can now store the entries of the JSON file in a much more readable way.
      The other higher-order functions can be used in the same way as map() with cities now being the supplied iterable.
         a) map()
         b) filter()
         c) reduce()
"""

import json
from collections import namedtuple
from functools import reduce

city = namedtuple("city", ["name", "country", "coordinates", "continent"])

with open('cities.json') as json_file:
  data = json.load(json_file) 

cities = map(lambda x: city(x["name"], x["country"], x["coordinates"], x["continent"]), data["city"])

# Code for Checkpoint 1 goes here.
a = filter(lambda x: x.continent == 'Asia', cities)
asia = tuple(a)
print(asia)

west = None

# Code for Checkpoint 2 goes here.
west = reduce(lambda x, y: x if x.coordinates[1] < y.coordinates[1] else y, asia)
print(west)
