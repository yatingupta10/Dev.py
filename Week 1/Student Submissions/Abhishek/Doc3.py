"""Question 3: 
WAP to input no. of fruits and their names. Also save these in a list. """

no = input("No of fruits please! \n")
#print no 

fruits = []
for i in range(no):
	print ("Enter the %s fruit: "%(i+1))
	fruit = raw_input()
	fruits.append(fruit)

print fruits