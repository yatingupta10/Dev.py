num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

sum = num1 + num2
print("sum of " + str(num1) + "+" + str(num2) + ":" + str(sum))

diff = num1 - num2
print("diff of " + str(num1) + "-" + str(num2) + ":" + str(diff))

mul = num1 * num2
print("mul of " + str(num1) + "*" + str(num2) + ":" + str(mul))

div = num1 // num2
print("div of " + str(num1) + "/" + str(num2) + ":" + str(div))
num2 = float(num2)

div_f = num1 / num2
print("div of " + str(num1) + "/" + str(num2) + "in float:" + str(div_f))

num2 = int(num2)
mod = num1 % num2
print("mod of " + str(num1) + "%" + str(num2) + ":" + str(mod))