def getGCD(q,div):

    while div%q!=0:
        nxtQ=div%q
        div=q
        q=nxtQ
    return q


num1=int(raw_input("enter number 1:"))
num2=int(raw_input("enter number 2:"))

if num1>num2:
    print getGCD(num2,num1)
else:
    print getGCD(num1,num2)
