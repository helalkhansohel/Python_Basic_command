
#-----------Class-----------------------------
#-------basic -------
class MyClass:
 x=555

p1=MyClass()
print(p1.x)

#All classes have a function called __init__(), which is always executed when the class is being initiated.

class StanderdClass:

  def __init__(self,name ,age):
    self.name=name
    self.age=age
  def myfunc(self):
    print("Hello my name is " + self.name)

p1=StanderdClass("Helal",26)
print(p1.name)
p1.myfunc()
del p1.age
del p1

class Person:
  pass

#--------------------------inheritance ----------------------Inheritance allows us to define a class that inherits all the methods and properties from another class.
class Person1: #Parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person1): #child class ,this class can use it's own property and mother class poperty
  def __init__(self, fname, lname):
    Person1.__init__(self, fname, lname) #or  super().__init__(fname, lname)
    self.graduationyear = 2019

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen")
x.printname()
