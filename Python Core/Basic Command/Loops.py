# ------loop 1--------------------
def Loop1():
    for x in range(1, 5, 1):
        print(x)


def Loop2():
    i = 0
    while i < 6:
        print(i)
        i += 1


def Loop3():
    i = 0
    while i < 6:
        print(i)
        if (i == 3):
            break
        i += 1


def Loop4():
    i = 1
    while i < 6:
        print(i)
        if (i == 3):
            i += 1
            break


def Loop5():
    i = 1
    while i < 6:
        print(i)
        if (i < 5):
            print(",")
        i += 1
    else:
        print("Loop finished ")


def Loop6():
    for x in range(6):
        print(x)
    else:
        print("Loop finsih ")


def Loop7():
    for x in range(1, 10, 2):
        print(x)


def Loop8():
    for x in [0, 1,
              2]:  # for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
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


#-------------Check--------------------------------------
def Check():
  txt = "The rain in Spain stays mainly in the plain"
  x = "ain" in txt
  print(x)

