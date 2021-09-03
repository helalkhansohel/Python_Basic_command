

""" Python basic """
#----------Global-------------------------
a=0 #global
b=0 #global

def myfunc(): 
  global a #To change the value of a global variable inside a function, refer to the variable by using the global keyword:
  a = 200
#---------------------------Functions------------------------------------------

#---------print function------------------
def MyPrint():
  x="Python"
  print("Hello Python")

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


#-------------------Variabls-------------------------

def Variables():

  global c #global variable inside function and initialize it in another line.
  c=0

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
  z =  x + y
  print(z)
  


#---------Conditions 1--------------
def Condifion1():
  num=0
  num=int(input("Please enter your Score :"))
  #and ,or 
  if num <60:
   print("Grade F")
  elif num>=60 and num<70:
   print("Grade D")
  elif num>=70 and num<80:
   print("Grade C")
  elif num>=80 and num<90:
   print("Grade B") 
  elif num>=90 and num<=100:
   print("Grade D")
  else:
   print("Wrong input")
def Condition2():
  x=41
  if x > 10:
   print("Above ten,")
   if x > 20:
     print("and also above 20!")
   else:
     print("but not above 20.")
  else:
    print("but not above 10.") 

#------loop 1--------------------
def Loop1():
 for x in range(1,5,1):
  print(x)

def Loop2():
  i=0
  while i<6:
   print(i)
   i+=1

def Loop3():
 i=0
 while i<6:
  print(i)
  if(i==3):
   break
  i += 1
  
def Loop4():
 i = 1
 while i < 6:
  print(i)
  if(i==3):
   i += 1  
   break
   
def Loop5():
 i=1
 while i<6:
  print(i)
  if(i<5):
   print(",")
  i+=1 
 else:
   print("Loop finished ") 

def Loop6():
  for x in range(6):
    print(x)
  else:
    print("Loop finsih ")

def Loop7():
  for x in range(1,10,2):
    print(x)

def Loop8():
  for x in [0, 1, 2]: #for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
   pass
def Loop9():
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
    if x == "banana":
      continue
    print(x)

def Loop10():
  adj = ["red", "big", "tasty"]
  fruits = ["apple", "banana", "cherry"]

  for x in adj:
    for y in fruits:
      print(x, y)

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

#------------------String------------------------------
def String():
  a = """Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
  sed do eiusmod tempor incididunt
  ut labore et dolore magna aliqua."""
  print(a)

  a = '''Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
  sed do eiusmod tempor incididunt
  ut labore et dolore magna aliqua.'''
  print(a)
  
  a = "Hello, World!"
  print(a[1]) # e

  #Get the characters from position 2 to position 4 
  b = "Hello, World!"
  print(b[2:5]) #llo

  #Get the characters from position 5 to position 3, starting the count from the end of the string:
  b = "Hello, World!"
  print(b[-5:-2]) #orl
  
  #Lenght
  a = "Hello, World!" 
  print(len(a)) #13

  #Count
  txt = "I love apples, apple are my favorite fruit"
  x = txt.count("apple")
  print(x) #2

  #The strip() , rstrip ,lstrip
  # method removes any whitespace from the beginning or the end , right end ,and laft end:
  txt = "     banana     "

  x = txt.strip()
  print("of all fruits", x, "is my favorite") #of all fruits banana is my favorite

  x = txt.rstrip()
  print("of all fruits", x, "is my favorite") #of all fruits      banana is my favorite

  x = txt.lstrip()
  print("of all fruits", x, "is my favorite") #of all fruits banana      is my favorite

  #rstrip , lstrip ,strip  *********
  #clean selected data form righr , left and both sides
  txt = "..banana,,,,,ssqqqww....."
  x = txt.rstrip(",.qsw") 
  print(x) #..banana

  txt = ",,,,,ssaaww.....banana.."
  x = txt.lstrip(",.asw")
  print(x) #banana..

  txt = "..banana,,,,,ssqqqww....."
  x = txt.strip(",.qsw")
  print(x) #banana



  #isspace
  txt = "   "
  x = txt.isspace()
  print(x) #True
  
  #The lower()
  a = "Hello, World!"
  print(a.lower())

  #The upper()
  a = "Hello, World!"
  print(a.upper())


  #swapcase()
  #Make the lower case letters upper case and the upper case letters lower case:
  txt = "Hello My Name Is PETER"
  x = txt.swapcase()
  print(x)#hELLO mY nAME iS peter

  #Relace
  a = "Hello, World!"
  print(a.replace("H", "J"))

  #The split()
  #splits the string into substrings
  a = "Hello, World!"
  print(a.split(",")) # returns ['Hello', ' World!']

  # rsplit
  #Split a string into a list
  txt = "apple, banana, cherry"
  x = txt.rsplit(", ")
  print(x) #['apple', 'banana', 'cherry']

  #splitlines()
  txt = "Thank you for the music\nWelcome to the jungle"
  x = txt.splitlines()
  print(x) # ['Thank you for the music', 'Welcome to the jungle']

  #join
  myTuple = ["John", "Peter", "Vicky"]
  x = "#".join(myTuple)
  print(x) #John#Peter#Vicky

  #partition
  #Search for the word "bananas", and return a tuple with three elements:
  txt = "I could eat bananas all day"
  x = txt.partition("bananas")
  print(x) #('I could eat ', 'bananas', ' all day')

  #check in
  txt = "The rain in Spain stays mainly in the plain"
  x = "ain" in txt
  print(x) #true

  #check Not in
  txt = "The rain in Spain stays mainly in the plain"
  x = "ain" not in txt
  print(x) #false

  #lstrip *****
  #Remove the leading characters:
  txt = ",,,,,ssaaww.....banana"
  x = txt.lstrip(",.asw")
  print(x)#banana

  #capitalize & txt.title()
  txt = "the is my age."
  x = txt.capitalize() #The is my age
  print (x)  

  #istitle
  #Check if each word start with an upper case letter:
  txt = "Hello, And Welcome To My World!"
  x = txt.istitle()
  print(x) #true


  #casefold or lower
  txt = "Hello, And Welcome To My World!"
  x = txt.casefold() #hello, and welcome to my world!
  print(x)

  #Center
  #add white space to left
  txt = "banana"
  x = txt.center(60) # "         banana "               
  print(x)

  #ljust
  #add white space to right
  txt = "banana"
  x = txt.ljust(20)
  print(x, "is my favorite fruit.") #banana              is my favorite fruit.

  #startswith
  #string.startswith(value, start, end)
  txt = "Hello, welcome to my world."
  x = txt.startswith("Hello")
  print(x) #True


  #endswith
  #string.endswith(value, start, end)
  #Check if the string ends with a punctuation sign (.):
  txt = "Hello, welcome to my world."
  x = txt.endswith(".")
  print(x) #True

  #find ->select first find
  #rfind->select the last find
  #override: string.find(value, start, end)/string.rfind(value, start, end) 
  #stat=where to start search , end =where to end search .
  
  #find is better then index as it returns -1 if don;t get any value.
  txt = "Hello, world to my world."
  x = txt.find("world")
  y = txt.rfind("world")
  print(x) #7
  print(y) #19


  #index & rindex ->string.index(value, start, end) & string.index(value, start, end)
  txt = "Hello, welcome to my world."
  x = txt.index("welcome")
  print(x) #7

  #isalnum() 
  #Check if all the characters in the text are alphanumeric:
  txt1 = "Company12"
  txt2 = "Company 12"
  x = txt1.isalnum()
  y = txt2.isalnum()
  print(x) #true
  print(y) #false

  #isdecimal or isdigit or  txt.isnumeric()
  #0 to infinity int number
  a = "\u0030" #unicode for 0
  b = "\u0047" #unicode for G

  print(a.isdecimal()) #true
  print(b.isdecimal()) #false

  #isidentifier
  #it can be identifier or variable or not
  a = "MyFolder"
  b = "Demo002"
  c = "2bring"
  d = "my demo"
  print(a.isidentifier())#true
  print(b.isidentifier())#true
  print(c.isidentifier())#false
  print(d.isidentifier())#false

  #islower
  a = "Hello world!"
  b = "hello 123"
  c = "mynameisPeter"
  print(a.islower()) #false
  print(b.islower()) #true
  print(c.islower()) #false

  #isuppur
  a = "Hello World!"
  b = "hello 123"
  c = "MY NAME IS PETER"

  print(a.isupper())#false
  print(b.isupper())#false
  print(c.isupper())#True

  #isprintable
  txt1 = "Hello!\nAre you #1?"
  txt2 = "Hello! Are you #1?"
  x = txt1.isprintable()
  y = txt2.isprintable()
  print(x)

  #zfill()
  #Fill the string with zeros until it is 10 characters long:
  txt = "50"
  x = txt.zfill(10)
  print(x) #0000000050


#-------------------------RegEx -----------------------------------------
#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.

def RegEx():
  import re
#-------------Search---------------------------------------------------------
  #search	Returns a Match object if there is a match anywhere in the string
  txt="The rain is Spain"
  x=re.search("^The.*spain$",txt)
  print(x) #true 

  # check that a specific word exists or not 
  x=re.search("Spain",txt)
  print(x) #true 

  x=re.search("India",txt)
  print(x) #None

  #Search for the first white-space character in the string:
  #You can use for other char too
  txt = "The rain in Spain"
  x = re.search("\s", txt)
  print("The first white-space character is located in position:", x.start()) #The first white-space character is located in position: 3

#------------------findall-----------------------------------
  #Return a list containing every occurrence of "ai":
  #Return an empty list if no match was found:
  txt = "The rain in Spain"
  x = re.findall("ai", txt)
  print(x) #['ai', 'ai']

  x = re.findall("\s", txt)
  print(x) #[' ', ' ',' ']

  
#-------------------------Split------------------------------------------
  
  #Split the string at every white-space character and make it a list:
  #You can use it for , and other char too
  txt = "The rain in Spain"
  x = re.split("\s", txt)
  print(x) #['The', 'rain', 'in', 'Spain']

  #Split the string at the first white-space character:
  txt = "The rain in Spain"
  x = re.split("\s", txt, 1)
  print(x) #['The', 'rain in Spain']

  x = re.split("\s", txt, 2)
  print(x) #['The', 'rain', 'in Spain']

#---------------------sub---------------------------------------------------
#Replace every white-space character with the number 9:
  txt = "The rain in Spain"
  x = re.sub("\s", "9", txt) #The9rain9in9Spain
  print(x)
  #Replace the first 2 occurrences:
  x = re.sub("\s", "9", txt, 2)
  print(x)#The9rain9in Spain

#------String ,group() and span------------------------
  
  txt = "The rain in Spain"
  x = re.search(r"\bS\w+", txt)

  #Search for an upper case "S" character in the beginning of a word, and print its position:
  print(x.span()) #(12, 17)
  print(x.string) #The rain in Spain Spain
  #Search for an upper case "S" character in the beginning of a word, and print the word:
  print(x.group()) #Spain

  #-----------------------------Use of find all----------------------------------------------

  #Find all lower case characters alphabetically between "a" and "m":

  x = re.findall("[a-m]", txt)
  print(x) #['h', 'e', 'a', 'i', 'i', 'a', 'i']

  #Find all digit characters:
  txt = "That will be 59 dollars"

  x = re.findall("\d", txt)
  print(x)#['5', '9']

  #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
  txt = "hello world"
  x = re.findall("he..o", txt)
  print(x)#['hello']
  #or
  txt = "hello world hello"
  x = re.findall("he..o", txt)
  print(x)# ['hello', 'hello']

  #Check if the string starts with 'hello':
  x = re.findall("^hello", txt) #x can be used as bool also
  #Check if the string ends with 'world':
  x = re.findall("world$", txt)

  #Check if the string contains "a" followed by exactly two "l" characters:
  txt = "The rain in Spain falls mainly in the plain!"
  x = re.findall("al{2}", txt)
  print(x) #['all'] ,x can be used as bool also

  #Check if the string contains either "falls" or "stays":
  txt = "The rain in Spain falls mainly in the plain!"
  x = re.findall("falls|stays", txt)

  print(x)#['falls']  ,x can be used as bool also

#-----------------------------------------------------
  txt = "The rain in Spain"
  #Check if the string starts with "The":
  x = re.findall("\AThe", txt)
  ##Check if "ain" is present at the beginning of a WORD:
  x = re.findall(r"\bain", txt)
  print(x)#false
  ##Check if "ain" is present at the end of a WORD:
  x = re.findall(r"ain\b", txt)
  #Check if "ain" is present, but NOT at the beginning of a word:
  x = re.findall(r"\Bain", txt)
  #Check if "ain" is present, but NOT at the end of a word:
  x = re.findall(r"ain\B", txt)
  #Check if the string contains any digits (numbers from 0-9):
  x = re.findall("\d", txt) #false
  #Return a match at every white-space character:
  x = re.findall("\s", txt)#[' ', ' ', ' ']
  #Return a match at every NON white-space character:
  x = re.findall("\S", txt) # or x = re.findall("\w", txt)
  #['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']

  ##Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
  x = re.findall("\W", txt)
  print(x)#[' ', ' ', ' ']

  #Check if the string ends with "Spain":
  x = re.findall("Spain\Z", txt)

  #Check if the string has any a, r, or n characters:
  x = re.findall("[arn]", txt)#['r', 'a', 'n', 'n', 'a', 'n']

  #Check if the string has any characters between a and n:
  x = re.findall("[a-n]", txt)#['h', 'e', 'a', 'i', 'n', 'i', 'n', 'a', 'i', 'n']

  #Check if the string has other characters than a, r, or n:
  x = re.findall("[^arn]", txt)# ['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']

  #Check if the string has any 0, 1, 2, or 3 digits:
  txt = "The rain in Spain"
  x = re.findall("[0123]", txt) #[]
  

  #Check if the string has any digits:
  txt = "8 times before 11:45 AM"
  x = re.findall("[0-9]", txt) #['8', '1', '1', '4', '5']

  #Check if the string has any two-digit numbers, from 00 to 59:
  txt = "8 times before 11:45 AM"
  x = re.findall("[0-5][0-9]", txt) #['11', '45']

  ##Check if the string has any characters from a to z lower case, and A to Z upper case:
  txt = "8 times before 11:45 AM"
  x = re.findall("[a-zA-Z]", txt) #['t', 'i', 'm', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'A', 'M']

  ##Check if the string has any + characters:
  txt = "8 times before 11:45 AM"
  x = re.findall("[+]", txt) #[] 











#------------------Random--------------------------------


def Random():
 import random as r
 print(r.randrange(1,10))
#-------------Check--------------------------------------
def Check():
  txt = "The rain in Spain stays mainly in the plain"
  x = "ain" in txt
  print(x)


#------------------Connect to MSSQl database------------------------------
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
import pyodbc # to get this write in terminal : pip install pyodbc
def ConnectToSQL():
  
 server = 'DESKTOP-TL74A5V' 
 database = 'Test' 
 username = 'sa' 
 password = 'sa123456' 
 cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
 cursor = cnxn.cursor()

 cursor.execute('SELECT * FROM HrmEmployee')

 for row in cursor:
    print(row)
    
 cursor.close() 
 
 print("close")
  
#---------------------List +Tuple +Sets------------------------------------------

""" 
List is a collection which is ordered and changeable. Allows duplicate members. []
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.()
Set is a collection which is unordered and unindexed. No duplicate members.{}
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""
def List_Tuple_Sets():
  #Create a List:
  thislist = ["apple", "banana", "cherry"]
  print(thislist)

  #Print all items in the list, one by one:
  thislist = ["apple", "banana", "cherry"]
  for x in thislist:
    print(x)

  #Print the second item of the list:
  thislist = ["apple", "banana", "cherry"]
  print(thislist[1])

  #Print the last item of the list:
  thislist = ["apple", "banana", "cherry"]
  print(thislist[-1])

  #Return the third, fourth, and fifth item:
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
  print(thislist[2:5])

  #This example returns items from 0 to 3:
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
  print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']

  #This will return the items from index 2 to the end.
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
  print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']

  #This example returns the items from index -4 (included) to index -1 (excluded)
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
  print(thislist[-4:-1])

  

  #Update the second item:
  thislist = ["apple", "banana", "cherry"]
  thislist[1] = "blackcurrant"
  print(thislist)

  #Check if "apple" is present in the list:
  thislist = ["apple", "banana", "cherry"]
  if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

  #Print the number of items in the list:
  thislist = ["apple", "banana", "cherry"]
  print(len(thislist))  

  #Using the append() method to add an item:
  thislist = ["apple", "banana", "cherry"]
  thislist.append("orange")
  print(thislist)

  #The remove() method removes the specified item:
  thislist = ["apple", "banana", "cherry"]
  thislist.remove("banana")
  print(thislist)

  #The pop() method removes the specified index, (or the last item if index is not specified):
  #thislist.pop(1) pop with position
  thislist = ["apple", "banana", "cherry"]
  thislist.pop()
  print(thislist)

  #The del keyword can also delete the list completely:
  thislist = ["apple", "banana", "cherry"]
  del thislist

  #The clear() method empties the list:
  thislist = ["apple", "banana", "cherry"]
  thislist.clear()
  print(thislist)

  #Make a copy of a list with the copy() method:
  thislist = ["apple", "banana", "cherry"]
  mylist = thislist.copy()
  print(mylist)

  #Join two list:
  list1 = ["a", "b" , "c"]
  list2 = [1, 2, 3]

  list3 = list1 + list2
  print(list3)

  #Append list2 into list1:
  list1 = ["a", "b" , "c"]
  list2 = [1, 2, 3]

  for x in list2:
    list1.append(x)

  print(list1)

  #count
  #How many times 5 number is in the list:
  thistuple = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]
  x = thistuple.count(5)
  print(x)

  #Reverse
  #Reverse the order of the fruit list:
  fruits = ['apple', 'banana', 'cherry']
  fruits.reverse()
  print(fruits)

  #Tuple to List and #List to tuple: --------------------------------Tuple 
  Tuple=("apple", "banana", "cherry")
  y = list(Tuple)
  x = tuple(y)
  print(y)
  
  #The tuple() Constructor
  thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
  print(thistuple)
  #Note: all the above method of list is applicable for Tuple except reverse ,append

  
  #sets:                                 --------------------------set
  thisset = {"apple", "banana", "cherry"}
  print(thisset)
  thisset.add("orange") #{'apple', 'orange', 'banana', 'cherry'}
  thisset.update(["orange", "mango", "grapes"])
  print(thisset) #{'mango', 'apple', 'orange', 'grapes', 'banana', 'cherry'}

#---------------------------Dictionaries------------------------------------
def Dictionaries():
  thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  #print value
  for x in thisdict:
    print(thisdict[x]) #Ford 
                       #Mustang 
                       #1964 
  #or
  for x in thisdict.values():
    print(x)

  #print variable
  for x in thisdict:
    print(x)  #brand 
              #model 
              #year
  
  #print both 
  for x, y in thisdict.items():
    print(x, y) #brand Ford
                #model Mustang
                #year 1964


  #Get single value
  print(thisdict["model"]) #Mustang

  #Change Value:
  thisdict["year"] = 2018
  thisdict["color"] = "red"
  print(thisdict)
 
  #pop()
  #Remove Item
  #del thisdict["model"] (same work)
  #thisdict.popitem()  (remove last item)
  thisdict.pop("model")
  print(thisdict)
  
  #find
  if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

  #length
  print(len(thisdict)) #3


  #Copy list:
  #myNewdict=dict(thisdict) (same)
  myNewdict = thisdict.copy()
  
  #empties the dictionary:
  thisdict.clear()
  #delete the list
  del thisdict

#------------Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

#or
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)


#------Lambda , it is use for expression ------------------
def LambdaExpression():

  x = lambda a : a + 10
  print(x(5))

  x = lambda a, b : a * b
  print(x(5, 6))

  x = lambda a, b, c : a + b + c
  print(x(5, 6, 2))

#----------------Array -----------
def Array():
  cars = ["Ford", "Volvo", "BMW"]
  print(cars) 
  #Note: check list 

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


#------------------------------Date------------------------

def MyDateTime():
  import datetime

  x=datetime.datetime.now
  print(x)
  print(x.year)
  print(x.strftime("%A")) #Week Day
  print(x.strftime("%B")) #month

  x = datetime.datetime(2020, 5, 17)

  print(x)

"""
%a	Weekday, short version                           ->	Wed	
%A	Weekday, full version	                           ->Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday             ->	3	
%d	Day of month 01-31                               ->	31	
%b	Month name, short version	                       ->Dec	
%B	Month name, full version	                       ->December	
%m	Month as a number 01-12	                         ->12	
%y	Year, short version, without century	->18	
%Y	Year, full version	->2018	
%H	Hour 00-23 ->	17	
%I	Hour 00-12	->05	
%p	AM/PM	->PM	
%M	Minute 00-59	->41	
%S	Second 00-59	->08	
%f	Microsecond 000000-999999	->548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366 ->	365	
%U	Week number of year, Sunday as the first day of week, 00-53	->52	
%W	Week number of year, Monday as the first day of week, 00-53	->52	
%c	Local version of date and time ->	Mon Dec 31 17:41:00 2018	
%x	Local version of date	-> 12/31/18	
%X	Local version of time ->	17:41:00	
%%	A % character	-> %	

"""

#------------------------------Math ---------------------------------------
def MinMax():
  x = min(5, 10, 25)
  y = max(5, 10, 25)

  print(x)
  print(y)

  #or
  a=(5, 10, 25)
  x = min(a)
  y = max(a)
  print(x)
  print(y)

  #pow
  x = pow(4, 3)
  print(x) #64

  #abs()
  x = abs(-7.25) #The abs() function returns the absolute (positive) value of the specified number:
  print(x) #7.25

def MothWithImportfunction(): 
 import math
 x = math.sqrt(64) #root
 print(x) #4

#Round a number upward to its nearest integer
 x = math.ceil(1.4)

#Round a number downward to its nearest integer
 y = math.floor(1.4)
 print(x)
 print(y)

 x = math.pi #PI

 print(x)

#-------------------JSON----------------------------------
def MyJson():
  import json
  #Convert from JSON to Python:
  x='{"Name":"Helal" ,"age":26}'
  y=json.loads(x)
  print(y["Name"])

  #Convert from Python to JSON:
  x={
    "name": "John",
    "age": 30,
    "city": "New York"
  }

  y=json.dumps(x)
  print(y)

  #Convert Python objects into JSON strings, and print the values:
  print(json.dumps({"name": "John", "age": 30}))
  print(json.dumps(["apple", "bananas"]))
  print(json.dumps(("apple", "bananas")))
  print(json.dumps("hello"))
  print(json.dumps(42))
  print(json.dumps(31.76))
  print(json.dumps(True))
  print(json.dumps(False))
  print(json.dumps(None))



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



