# ---------------------List +Tuple +Sets------------------------------------------

"""
List is a collection which is ordered and changeable. Allows duplicate members. []
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.()
Set is a collection which is unordered and unindexed. No duplicate members.{}
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""


def List_Tuple_Sets():
    # Create a List:
    thislist = ["apple", "banana", "cherry"]
    print(thislist)

    # Print all items in the list, one by one:
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)

    # Print the second item of the list:
    thislist = ["apple", "banana", "cherry"]
    print(thislist[1])

    # Print the last item of the list:
    thislist = ["apple", "banana", "cherry"]
    print(thislist[-1])

    # Return the third, fourth, and fifth item:
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])

    # This example returns items from 0 to 3:
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[:4])  # ['apple', 'banana', 'cherry', 'orange']

    # This will return the items from index 2 to the end.
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:])  # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

    # This example returns the items from index -4 (included) to index -1 (excluded)
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-4:-1])

    # Update the second item:
    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist)

    # Check if "apple" is present in the list:
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")

    # Print the number of items in the list:
    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))

    # Using the append() method to add an item:
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)

    # The remove() method removes the specified item:
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist)

    # The pop() method removes the specified index, (or the last item if index is not specified):
    # thislist.pop(1) pop with position
    thislist = ["apple", "banana", "cherry"]
    thislist.pop()
    print(thislist)

    # The del keyword can also delete the list completely:
    thislist = ["apple", "banana", "cherry"]
    del thislist

    # The clear() method empties the list:
    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)

    # Make a copy of a list with the copy() method:
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)

    # Join two list:
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list3 = list1 + list2
    print(list3)

    # Append list2 into list1:
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    for x in list2:
        list1.append(x)

    print(list1)

    # count
    # How many times 5 number is in the list:
    thistuple = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]
    x = thistuple.count(5)
    print(x)

    # Reverse
    # Reverse the order of the fruit list:
    fruits = ['apple', 'banana', 'cherry']
    fruits.reverse()
    print(fruits)

    # Tuple to List and #List to tuple: --------------------------------Tuple
    Tuple = ("apple", "banana", "cherry")
    y = list(Tuple)
    x = tuple(y)
    print(y)

    # The tuple() Constructor
    thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
    print(thistuple)
    # Note: all the above method of list is applicable for Tuple except reverse ,append

    # sets:                                 --------------------------set
    thisset = {"apple", "banana", "cherry"}
    print(thisset)
    thisset.add("orange")  # {'apple', 'orange', 'banana', 'cherry'}
    thisset.update(["orange", "mango", "grapes"])
    print(thisset)  # {'mango', 'apple', 'orange', 'grapes', 'banana', 'cherry'}


# ---------------------------Dictionaries------------------------------------
def Dictionaries():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    # print value
    for x in thisdict:
        print(thisdict[x])  # Ford
        # Mustang
        # 1964
    # or
    for x in thisdict.values():
        print(x)

    # print variable
    for x in thisdict:
        print(x)  # brand
        # model
        # year

    # print both
    for x, y in thisdict.items():
        print(x, y)  # brand Ford
        # model Mustang
        # year 1964

    # Get single value
    print(thisdict["model"])  # Mustang

    # Change Value:
    thisdict["year"] = 2018
    thisdict["color"] = "red"
    print(thisdict)

    # pop()
    # Remove Item
    # del thisdict["model"] (same work)
    # thisdict.popitem()  (remove last item)
    thisdict.pop("model")
    print(thisdict)

    # find
    if "model" in thisdict:
        print("Yes, 'model' is one of the keys in the thisdict dictionary")

    # length
    print(len(thisdict))  # 3

    # Copy list:
    # myNewdict=dict(thisdict) (same)
    myNewdict = thisdict.copy()

    # empties the dictionary:
    thisdict.clear()
    # delete the list
    del thisdict

    # ------------Create a dictionary that contain three dictionaries:
    myfamily = {
        "child1": {
            "name": "Emil",
            "year": 2004
        },
        "child2": {
            "name": "Tobias",
            "year": 2007
        },
        "child3": {
            "name": "Linus",
            "year": 2011
        }
    }

    print(myfamily)

    # or
    child1 = {
        "name": "Emil",
        "year": 2004
    }
    child2 = {
        "name": "Tobias",
        "year": 2007
    }
    child3 = {
        "name": "Linus",
        "year": 2011
    }

    myfamily = {
        "child1": child1,
        "child2": child2,
        "child3": child3
    }

    print(myfamily)


