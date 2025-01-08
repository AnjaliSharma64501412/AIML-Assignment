number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    square = number * number
    print("The square of", number, "is:", square)
