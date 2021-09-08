def Test(s, i):
    l = list(s)
    f = 0
    for x in l:
        if i == 1:
            if x.isalnum():
                f = 1
            else:
                f = 0
                break
        elif i == 2:
            if x.isalpha():
                f = 1
                break
        elif i == 3:
            if x.isdigit():
                f = 1
                break
        elif i == 4:
            if x.islower():
                f = 1
                break
        elif i == 5:
            if x.isupper():
                f = 1
                break
        else:
            pass

    if f == 1:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    s = input()

    Test(s, 1)
    Test(s, 2)
    Test(s, 3)
    Test(s, 4)
    Test(s, 5)