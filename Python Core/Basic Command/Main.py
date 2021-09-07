

#----------------Gatting value from function ------------

def myFunction():
  return True

def my_function(fname):
  print(fname + " Refsnes")

#my_function("Emil")

def my_function2(**kid):
  print("His last name is " + kid["lname"])

#my_function2(fname = "Tobias", lname = "Refsnes")

def my_function3(child3, child2, child1):
  print("The youngest child is " + child3)

#my_function3(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function4(*kids):
  print("The youngest child is " + kids[2])

#my_function4("Emil", "Tobias", "Linus")

def my_function5(x,y,z):
  print("The youngest child is " + z)

#my_function5("Emil", "Tobias", "Linus")

def my_function6(country = "Norway"): #defaul parameter
  print("I am from " + country)

#my_function6("India")
#my_function6()

#-----------------array function---------
def my_function7(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

#my_function7(fruits)

# --- Return value function-
def my_function8(x):
  return 5 * x

y=my_function8(3)
print(y)

# Empty function
def myfunction9():
  pass

def FunctionCall():
 if myFunction():
  print("YES!")
 else:
  print("NO!") 






#----------------Array -----------
def Array():
  cars = ["Ford", "Volvo", "BMW"]
  print(cars) 
  #Note: check list 

#-------try expect finall/else
def tryExcept():
  try:
   print(x)
  except:
   print("Something went wrong")
  finally: #or else
   print("The 'try except' is finished")

#------Iterators--------------------------
"""
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
"""
def Iterration():
  mytuple = ("apple", "banana", "cherry")
  myIter=iter(mytuple)
  print(next(myIter))
  print(next(myIter))
  print(next(myIter))

  """out put:
  apple
  banana
  cherry
   """


def IterrationStrings():

  mytuple = "test"

  obj=iter(mytuple)
  print(obj)
  print(obj)
  print(obj)
  print(obj)


#or
 
  for x in mytuple:
   print(x)

  """
  Output:
  t
  e
  s
  t
  
  """

#---------------------Mobule--------------
#A file containing a set of functions you want to include in your application.
def CallFunctionfromAnotherPage():

  import myModule

  myModule.greeting("Jonathan")



#----------Function call-----------------------------------------------------
print("---------------------Basic Python--------------------------")
#ConnectToSQL()
#FunctionCall()
#String()
#MyPrint()
#Check()
#Random()
#Variables()
#Loop1()
#Loop2()
#Loop3()
#Condition2()
#IOName()
#Condifion1()



