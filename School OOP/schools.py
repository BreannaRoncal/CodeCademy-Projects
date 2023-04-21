"""
Let’s put your knowledge of classes to the test by creating a digital school catalog for the New York City Department of Education. 
The Department of Education wants the catalog to hold quick reference material for each school in the city.

We need to create classes for primary and high schools. 
Because these classes share properties and methods, each will inherit from a parent School class. 
Our parent and three child classes have the following properties, getters, setters, and methods:

  School
    - Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents (integer)
    - Getters: all properties have getters
    - Setters: the numberOfStudents property has a setter
    - Methods: A __repr__ method that displays information about the school.
  
  Primary
    - Includes everything in the School class, plus one additional property
    - Properties: pickupPolicy (string, like "Pickup after 3pm")
  
  Middle
    - Does not include any additional properties or methods
  
  High
    - Includes everything in the School class, plus one additional property
    - Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])
    
"""

class School():
  def __init__(self, name, level, numberOfStudents):
    self._name = name
    self._level = level
    self._numberOfStudents = numberOfStudents

  def get_name(self):
    return self._name

  def get_level(self):
    return self._level

  def get_numberOfStudents(self):
    return self._numberOfStudents

  def set_numberOfStudents(self, new_num):
    if isinstance(new_num, int):
      self._numberOfStudents = new_num
    else:
      raise TypeError
  
  def __repr__(self):
    return "A " + self._level + " school named " + self._name + " with " + str(self._numberOfStudents) + " students"


class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "Primary", numberOfStudents)
    self._pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self._pickupPolicy

  def __repr__(self):
    parent_repr = super().__repr__()
    return parent_repr + " The pickup Policy is " + self._pickupPolicy

class MiddleSchool(School):
  def __init__(self, name, numberOfStudents):
    super().__init__(name, "Middle", numberOfStudents)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "High", numberOfStudents)
    self._sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return ", ".join(self._sportsTeams)

  def __repr__(self):
    parent_repr = super().__repr__()
    return parent_repr + " The sports teams are " + self.get_sportsTeams()
"""
# Test School Parent class
test_school = School("MSA", "Primary", 10)
print(test_school)
print(test_school.get_name())
print(test_school.get_level())
print(test_school.get_numberOfStudents())
test_school.set_numberOfStudents(100)
print(test_school.get_numberOfStudents())

# Test Primary School class
test_p = PrimarySchool("Overland", 100, "pickup by 5pm")
print(test_p.get_pickupPolicy())
print(test_p)


# Test Middle School class
test_m = MiddleSchool("Palms", 100)
print(test_m)
print(test_m.get_name())
print(test_m.get_level())
print(test_m.get_numberOfStudents())
"""
# Test High School class
sportsTeams = ["basketball", "volleyball", "soccer"]
test_h = HighSchool("UNI", 2000, sportsTeams)
print(test_h)
