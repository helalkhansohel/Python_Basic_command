
""" Python basic """
#----------Global-------------------------
a=0 #global
b=0 #global

def myfunc():
  global a #To change the value of a global variable inside a function, refer to the variable by using the global keyword:
  a = 200


#---------print function------------------
def MyPrint():
  x="Python"
  print("Hello Python")
  print("Age:",end=" ") # To print data in one line
  print("Hello " , x, "welcome")

  age = 36
  txt = "My name is John, I am " + str(age)
  print(txt)

  age = 36
  age1=37
  txt = "My name is John, and I am {} to {}"
  print(txt.format(age,age1))

  quantity = 3
  itemno = 567
  price = 49.95
  myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
  print(myorder.format(quantity, itemno, price))

  txt = "For only {price:.2f} dollars!"
  print(txt.format(price = 49))#For only 49.00 dollars!

  #named indexes:
  txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
  #numbered indexes:
  txt2 = "My name is {0}, I'm {1}".format("John",36)
  #empty placeholders:
  txt3 = "My name is {}, I'm {}".format("John",36)
  print(txt1)
  print(txt2)
  print(txt3)
  #formates https://www.w3schools.com/python/ref_string_format.asp

  txt = "We are the so-called \"Vikings\" from the north."
  print(txt)
#---------I/0 Function---------------------
def IOName():
  Name=input("Your Name ?")
  print("Name: ",Name)


# -------------------Variabls-------------------------

def Variables():
    global c  # global variable inside function and initialize it in another line.
    c = 0

    x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)

    x = y = z = "Orange"
    print(x)
    print(y)
    print(z)

    x = "Python is "
    y = "awesome"
    z = x + y
    print(z)



#--------------------dataType----------------------------
def dataType():
  x = 1    # int
  y = 2.8  # float
  z = 1j   # complex

  x = 1                 #int
  y = 35656222554887711 #int
  z = -3255522          #int

  x = 1.10    #float
  y = 1.0     #float
  z = -35.59  #float
  x = 35e3    #float
  y = 12E4
  z = -87.7e100
  x = 3+5j
  y = 5j
  z = -5j

  print(type(x))
  print(type(y))
  print(type(z))


#------------------Casting-----------------------------
def Casting():
  x = 1 # int
  y = 2.8 # float
  z = 1j # complex

  #convert from int to float:
  a = float(x)
  #convert from float to int:
  b = int(y)
  #convert from int to complex:
  c = complex(x)

  y = str(2)

  print(a)
  print(b)
  print(c)
  print(z)
