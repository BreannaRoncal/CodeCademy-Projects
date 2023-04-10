"""
Our friend has asked us to review and edit the introduction to their paper. 
Luckily the mistakes are all generally similar, such as misspellings of the same word and a repeated glitch from a software bug. 
This will require us to extend our naive pattern search algorithm functionality to not just find patterns, but replace them as well! 
This will be done through the following steps:

  1. Find patterns more easily by making the search case-insensitive.
  2. Build and maintain a separate copy of the introduction to insert replacements.
  3. Skip newly-replaced characters.
"""

def pattern_search(text, pattern, replacement, case_sensitive=True):
  fixed_text = ""
  num_skips = 0
  for index in range(len(text)):
    if num_skips > 0:
      num_skips -= 1
      continue
    match_count = 0
    for char in range(len(pattern)): 
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index) 
      fixed_text += replacement
      num_skips = len(pattern) - 1
    else:
      fixed_text += text[index]
  return fixed_text

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language", "language")
pattern_search(friends_intro, "pylhon", "Python", False)
pattern_search(friends_intro, "idil", "ideal", False)
pattern_search(friends_intro, "zzz ", "")
pattern_search(friends_intro, "syntacs", "syntax")
pattern_search(friends_intro, "languuUuage", "language")
