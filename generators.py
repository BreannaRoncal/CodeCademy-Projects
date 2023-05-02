"""
Python Generators

In this lesson, you learned how to:

  - Create generator functions using yield
  - Implement generator expressions
  - Use built-in generator methods like .send(), .throw(), and .close()
  - Connect generators into single generators
  - Use nested or pipelined generators
"""

def summa():
    yield 'Summa Cum Laude'
def magna():
    yield 'Magna Cum Laude' 
def cum_laude():
    yield 'Cum Laude'
    
# Write your code below:

"""
We have three honors achievements to assign to students that are defined within the summa(), magna(), and cum_laude() generator functions. 
Each honor is assigned based on a given GPA range listed below. 
Given a list of input GPAs, create a generator function called honors_generator that takes in 1 input argument named gpas that represents the list 
of GPAs from the variable gpas. The function should use yield from on each input GPA to determine the honors assignment.
"""
# Honors Generator
gpas = [3.2, 4.0, 3.6, 2.9]
def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()

# Test honors_generator()
honors = honors_generator(gpas)
for honor_label in honors:
  print(honor_label)

# Count Down Generator is the equivalent generator expression of the graduation_countdown() generator
days = 25
countdown_generator = (i for i in range(days, -1, -1))

def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left is not None:
      days = days_left
    else:
      days -= 1

# Test countdown_generator()
grad_days = graduation_countdown(days)
for i in grad_days:
  if i == 15:
    grad_days.send(10)
  elif i == 3:
    grad_days.close()
  print("Days Left: " + str(i))
