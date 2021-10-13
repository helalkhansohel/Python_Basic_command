if __name__ == '__main__':
    arr = list(map(int, input().split()))
    x=arr[0]
    k=arr[1]
    p=0
    T=0
    for i in range(0,k):

        p=x**(k-1)
        k=k-1
        T=T+p

    if T==arr[1]:
        print("True")
    else:
        print("False")
