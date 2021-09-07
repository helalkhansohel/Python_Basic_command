
# -------------------------RegEx -----------------------------------------
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

def RegEx():
    import re
    # -------------Search---------------------------------------------------------
    # search	Returns a Match object if there is a match anywhere in the string
    txt ="The rain is Spain"
    x=re.search("^The.*spain$",txt)
    print(x)  # t  ue

    # check that a specific word exists or not
    x=re.search("Spain",txt)
    print(x)  # t  ue

    x=re.search("India",txt)
    print(x)  # N  ne

    # Search for the first white-space character in the string:
    # You can use for other char too
    txt = "The rain in Spain"
    x = re.search("\s", txt)
    print("The first white-space character is located in position:", x.sart())  # T  e first white-space character is located in position: 3

    # ------------------findall-----------------------------------
    # Return a list containing every occurrence of "ai":
    # Return an empty list if no match was found:
    txt = "The rain in Spain"
    x = re.findall("ai", txt)
    print(x)  # [  ai', 'ai']

    x = re.findall("\s", txt)
    print(x)  # [   ', ' ',' ']

    # -------------------------Split------------------------------------------

    # Split the string at every white-space character and make it a list:
    # You can use it for , and other char too
    txt = "The rain in Spain"
    x = re.split("\s", txt)
    print(x)  # [  The', 'rain', 'in', 'Spain']

    # Split the string at the first white-space character:
    txt = "The rain in Spain"
    x = re.split("\s", txt, 1)
    print(x)  # [  The', 'rain in Spain']

    x = re.split("\s", txt, 2)
    print(x)  # [  The', 'rain', 'in Spain']

    # ---------------------sub---------------------------------------------------
    # Replace every white-space character with the number 9:
    txt = "The rain in Spain"
    x = re.sub("\s", "9", txt)  # T  e9rain9in9Spain
    print(x)
    # Replace the first 2 occurrences:
    x = re.sub("\s", "9", txt, 2)
    print(x)# Th  e9rain9in Spain

    # ------String ,group() and span------------------------

    txt = "The rain in Spain"
    x = re.search(r"\bS\w+", txt)

    # Search for an upper case "S" character in the beginning of a word, and print its position:
    print(x.span())  # (  2, 17)
    print(x.string)  # T  e rain in Spain Spain
    # Search for an upper case "S" character in the beginning of a word, and print the word:
    print(x.group())  # S  ain

    # -----------------------------Use of find all----------------------------------------------

    # Find all lower case characters alphabetically between "a" and "m":

    x = re.findall("[a-m]", txt)
    print(x)  # [  h', 'e', 'a', 'i', 'i', 'a', 'i']

    # Find all digit characters:
    txt = "That will be 59 dollars"

    x = re.findall("\d", txt)
    print(x)# ['  5', '9']

    # Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
    txt = "hello world"
    x = re.findall("he..o", txt)
    print(x)# ['  hello']
    # or
    txt = "hello world hello"
    x = re.findall("he..o", txt)
    print(x)# ['  hello', 'hello']

    # Check if the string starts with 'hello':
    x = re.findall("^hello", txt)  # x  can be used as bool also
    # Check if the string ends with 'world':
    x = re.findall("world$", txt)

    # Check if the string contains "a" followed by exactly two "l" characters:
    txt = "The rain in Spain falls mainly in the plain!"
    x = re.findall("al{2}", txt)
    print(x)  # [  all'] ,x can be used as bool also

    # Check if the string contains either "falls" or "stays":
    txt = "The rain in Spain falls mainly in the plain!"
    x = re.findall("falls|stays", txt)

    print(x)# ['  falls']  ,x can be used as bool also

    # -----------------------------------------------------
    txt = "The rain in Spain"
    # Check if the string starts with "The":
    x = re.findall("\AThe", txt)
    ##Check if "ain" is present at the beginning of a WORD:
    x = re.findall(r"\bain", txt)
    print(x)# fa  lse
    ##Check if "ain" is present at the end of a WORD:
    x = re.findall(r"ain\b", txt)
    # Check if "ain" is present, but NOT at the beginning of a word:
    x = re.findall(r"\Bain", txt)
    # Check if "ain" is present, but NOT at the end of a word:
    x = re.findall(r"ain\B", txt)
    # Check if the string contains any digits (numbers from 0-9):
    x = re.findall("\d", txt)  # f  lse
    # Return a match at every white-space character:
    x = re.findall("\s", txt)# ['   ', ' ', ' ']
    # Return a match at every NON white-space character:
    x = re.findall("\S", txt) # o   x = re.findall("\w", txt)
    # ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']

    ##Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
    x = re.findall("\W", txt)
    print(x)# ['   ', ' ', ' ']

    # Check if the string ends with "Spain":
    x = re.findall("Spain\Z", txt)

    # Check if the string has any a, r, or n characters:
    x = re.findall("[arn]", txt)# ['  r', 'a', 'n', 'n', 'a', 'n']

    # Check if the string has any characters between a and n:
    x = re.findall("[a-n]", txt)# ['  h', 'e', 'a', 'i', 'n', 'i', 'n', 'a', 'i', 'n']

    # Check if the string has other characters than a, r, or n:
    x = re.findall("[^arn]", txt)# ['  T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']

    # Check if the string has any 0, 1, 2, or 3 digits:
    txt = "The rain in Spain"
    x = re.findall("[0123]", txt)  # []

    # Check if the string has any digits:
    txt = "8 times before 11:45 AM"
    x = re.findall("[0-9]", txt)  # [  8', '1', '1', '4', '5']

    # Check if the string has any two-digit numbers, from 00 to 59:
    txt = "8 times before 11:45 AM"
    x = re.findall("[0-5][0-9]", txt)  # [  11', '45']

    ##Check if the string has any characters from a to z lower case, and A to Z upper case:
    txt = "8 times before 11:45 AM"
    x = re.findall("[a-zA-Z]", txt)  # [  t', 'i', 'm', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'A', 'M']

    ##Check if the string has any + characters:
    txt = "8 times before 11:45 AM"
    x = re.findall("[+]", txt)  # [









