

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
