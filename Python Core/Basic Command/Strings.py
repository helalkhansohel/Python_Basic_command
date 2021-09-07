# ------------------String------------------------------
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
    print(a[1])  # e

    # Get the characters from position 2 to position 4
    b = "Hello, World!"
    print(b[2:5])  # llo

    # Get the characters from position 5 to position 3, starting the count from the end of the string:
    b = "Hello, World!"
    print(b[-5:-2])  # orl

    # Lenght
    a = "Hello, World!"
    print(len(a))  # 13

    # Count
    txt = "I love apples, apple are my favorite fruit"
    x = txt.count("apple")
    print(x)  # 2

    # The strip() , rstrip ,lstrip
    # method removes any whitespace from the beginning or the end , right end ,and laft end:
    txt = "     banana     "

    x = txt.strip()
    print("of all fruits", x, "is my favorite")  # of all fruits banana is my favorite

    x = txt.rstrip()
    print("of all fruits", x, "is my favorite")  # of all fruits      banana is my favorite

    x = txt.lstrip()
    print("of all fruits", x, "is my favorite")  # of all fruits banana      is my favorite

    # rstrip , lstrip ,strip  *********
    # clean selected data form righr , left and both sides
    txt = "..banana,,,,,ssqqqww....."
    x = txt.rstrip(",.qsw")
    print(x)  # ..banana

    txt = ",,,,,ssaaww.....banana.."
    x = txt.lstrip(",.asw")
    print(x)  # banana..

    txt = "..banana,,,,,ssqqqww....."
    x = txt.strip(",.qsw")
    print(x)  # banana

    # isspace
    txt = "   "
    x = txt.isspace()
    print(x)  # True

    # The lower()
    a = "Hello, World!"
    print(a.lower())

    # The upper()
    a = "Hello, World!"
    print(a.upper())

    # swapcase()
    # Make the lower case letters upper case and the upper case letters lower case:
    txt = "Hello My Name Is PETER"
    x = txt.swapcase()
    print(x)  # hELLO mY nAME iS peter

    # Relace
    a = "Hello, World!"
    print(a.replace("H", "J"))

    # The split()
    # splits the string into substrings
    a = "Hello, World!"
    print(a.split(","))  # returns ['Hello', ' World!']

    # rsplit
    # Split a string into a list
    txt = "apple, banana, cherry"
    x = txt.rsplit(", ")
    print(x)  # ['apple', 'banana', 'cherry']

    # splitlines()
    txt = "Thank you for the music\nWelcome to the jungle"
    x = txt.splitlines()
    print(x)  # ['Thank you for the music', 'Welcome to the jungle']

    # join
    myTuple = ["John", "Peter", "Vicky"]
    x = "#".join(myTuple)
    print(x)  # John#Peter#Vicky

    # partition
    # Search for the word "bananas", and return a tuple with three elements:
    txt = "I could eat bananas all day"
    x = txt.partition("bananas")
    print(x)  # ('I could eat ', 'bananas', ' all day')

    # check in
    txt = "The rain in Spain stays mainly in the plain"
    x = "ain" in txt
    print(x)  # true

    # check Not in
    txt = "The rain in Spain stays mainly in the plain"
    x = "ain" not in txt
    print(x)  # false

    # lstrip *****
    # Remove the leading characters:
    txt = ",,,,,ssaaww.....banana"
    x = txt.lstrip(",.asw")
    print(x)  # banana

    # capitalize & txt.title()
    txt = "the is my age."
    x = txt.capitalize()  # The is my age
    print(x)

    # istitle
    # Check if each word start with an upper case letter:
    txt = "Hello, And Welcome To My World!"
    x = txt.istitle()
    print(x)  # true

    # casefold or lower
    txt = "Hello, And Welcome To My World!"
    x = txt.casefold()  # hello, and welcome to my world!
    print(x)

    # Center
    # add white space to left
    txt = "banana"
    x = txt.center(60)  # "         banana "
    print(x)

    # ljust
    # add white space to right
    txt = "banana"
    x = txt.ljust(20)
    print(x, "is my favorite fruit.")  # banana              is my favorite fruit.

    # startswith
    # string.startswith(value, start, end)
    txt = "Hello, welcome to my world."
    x = txt.startswith("Hello")
    print(x)  # True

    # endswith
    # string.endswith(value, start, end)
    # Check if the string ends with a punctuation sign (.):
    txt = "Hello, welcome to my world."
    x = txt.endswith(".")
    print(x)  # True

    # find ->select first find
    # rfind->select the last find
    # override: string.find(value, start, end)/string.rfind(value, start, end)
    # stat=where to start search , end =where to end search .

    # find is better then index as it returns -1 if don;t get any value.
    txt = "Hello, world to my world."
    x = txt.find("world")
    y = txt.rfind("world")
    print(x)  # 7
    print(y)  # 19

    # index & rindex ->string.index(value, start, end) & string.index(value, start, end)
    txt = "Hello, welcome to my world."
    x = txt.index("welcome")
    print(x)  # 7

    # isalnum()
    # Check if all the characters in the text are alphanumeric:
    txt1 = "Company12"
    txt2 = "Company 12"
    x = txt1.isalnum()
    y = txt2.isalnum()
    print(x)  # true
    print(y)  # false

    # isdecimal or isdigit or  txt.isnumeric()
    # 0 to infinity int number
    a = "\u0030"  # unicode for 0
    b = "\u0047"  # unicode for G

    print(a.isdecimal())  # true
    print(b.isdecimal())  # false

    # isidentifier
    # it can be identifier or variable or not
    a = "MyFolder"
    b = "Demo002"
    c = "2bring"
    d = "my demo"
    print(a.isidentifier())  # true
    print(b.isidentifier())  # true
    print(c.isidentifier())  # false
    print(d.isidentifier())  # false

    # islower
    a = "Hello world!"
    b = "hello 123"
    c = "mynameisPeter"
    print(a.islower())  # false
    print(b.islower())  # true
    print(c.islower())  # false

    # isuppur
    a = "Hello World!"
    b = "hello 123"
    c = "MY NAME IS PETER"

    print(a.isupper())  # false
    print(b.isupper())  # false
    print(c.isupper())  # True

    # isprintable
    txt1 = "Hello!\nAre you #1?"
    txt2 = "Hello! Are you #1?"
    x = txt1.isprintable()
    y = txt2.isprintable()
    print(x)

    # zfill()
    # Fill the string with zeros until it is 10 characters long:
    txt = "50"
    x = txt.zfill(10)
    print(x)  # 0000000050
