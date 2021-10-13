if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    MyList=list(arr) #Convert to List
    mylist = list(dict.fromkeys(MyList)) #Remove duplicates

    max=max(mylist) #find max

    mylist.remove(max) # Remove max

   # for x in mylist:
      #  print(x)
    l=len(mylist)
    runner=None
    for i in range(0,l):

        if (runner is None or mylist[i] > runner):
            runner = mylist[i]
    #Rurrer=max(mylist) #find Runner

    print(runner)



  #  print(Rurrer)
    #1 -1 -2 -1
    #57 57 -57 57