"""
Our friend has asked us to review and edit the introduction to their paper. 
Luckily the mistakes are all generally similar, such as misspellings of the same word and a repeated glitch from a software bug. 
This will require us to extend our naive pattern search algorithm functionality to not just find patterns, but replace them as well! 
This will be done through the following steps:

  1. Find patterns more easily by making the search case-insensitive.
  2. Build and maintain a separate copy of the introduction to insert replacements.
  3. Skip newly-replaced characters.
  
  
Replace Found Words:

  1. Maintaining the Fixed Text
      a) Add an additional replacement input parameter to the function definition for the text that will replace the found pattern.
      b) Initialize a fixed_text variable at the top of the function that will serve as a placeholder for the completed text containing 
         all the necessary replacements to be returned at the end of the function.
      c) When the pattern is found, the replacement should now be appended to the fixed_text. In all other cases, append the currently 
         iterating text character to the fixed_text to ensure that the rest of the original text is being maintained.
         
         
  2. Skipping Replaced Characters
      a) Initialize a num_skips variable set to 0 right after the initialization of the fixed_text variable. 
         This will track the numbers of characters that need to be skipped during the search, as a pattern was already found, and the relevant 
         characters in the text already replaced.
      b) While iterating through the text indices, if num_skips is greater than 0, decrement it by 1 and continue to the next iteration of the for loop. 
         This logic allows for the actual skipping of the replaced characters.
      c) Right after the replacement is appended to the fixed_text, set num_skips to the length of the pattern minus 1. 
         This sets the number of following search iterations to skip. 1 must be subtracted to account for the current iteration.
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
