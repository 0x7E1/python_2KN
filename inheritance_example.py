# Our super class
class Animal:
  limbsCount = 4


# Cat class inherits Animal class
class Cat(Animal):
  subspecies = "cat"
  name = ""
  
  # Constructor for Cat class
  def __init__(self, name):
    self.name = name


# Dog class inherits Animal class
class Dog(Animal):
  subspecies = "dog"
  name = ""
  
  # Constructor for Dog class
  def __init__(self, name):
    self.name = name


chloe = Cat("Chloe")
print ("This is %s. She's %s and has %s limbs." % (chloe.name, chloe.subspecies, chloe.limbsCount))

oliver = Dog("Oliver")
print ("This is %s. She's %s and has %s limbs." % (oliver.name, oliver.subspecies, oliver.limbsCount))