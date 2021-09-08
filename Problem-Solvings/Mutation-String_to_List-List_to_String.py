def mutate_string(string, position, character):

    data=list(string) #string to list
    data[position]=character
    mydata=""

    #list to string
    for x in data:
        mydata+=x
    return mydata

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)