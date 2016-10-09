count = int(input("Enter the number of fruits: "))

list = []
for i in range(count):
	fruit = raw_input("Enter the name of the fruit: ")
	list.append(fruit)

print(list)