def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%100==0:
        if year%400==0:
                return True
        else:
                return False
                   
    elif year%4==0:           
        
        return True             
    else:
        return False
    

year = int(input())

#n the Gregorian calendar, three conditions are used to identify leap years:

#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.