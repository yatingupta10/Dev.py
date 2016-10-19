
def printfibo(num):
    i=0
    first=0
    second=1
    print first
    print second

    while i<num:
        third=first+second
        first=second
        second=third
        print third
        i+=1


size=int(raw_input("enter size of series:"))
printfibo(size)
