
number = int(input("Enter an odd number: "))

if number <= 0 or number % 2 == 0:
    print("That's an even number, try again.")

else:
    for i in range(1, number+1, 2):
        print(("*" * i).center(number))

    for i in range(1, number-1, 2):
        print(("*" * (number - (i + 1))).center(number))