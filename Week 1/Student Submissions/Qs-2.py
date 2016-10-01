# 
#Perform addition, subtraction, multiplication, 
#division(real number and floating number), 
#mod/remainder. 
#

num1=int(raw_input())
num2=int(raw_input())

result=num1+num2
print "sum of "+str(num1)+"+"+str(num2)+":"+str(result)

result=num1-num2
print "diff of "+str(num1)+"-"+str(num2)+":"+str(result)

result=num1*num2
print "mul of "+str(num1)+"*"+str(num2)+":"+str(result)

result=num1/num2
print "div of "+str(num1)+"/"+str(num2)+":"+str(result)
num2=num2+0.0
result=num1/num2
print "div of "+str(num1)+"/"+str(num2)+"(in float):"+str(result)

result=num1%num2
print "mod of "+str(num1)+"%"+str(num2)+":"+str(result)