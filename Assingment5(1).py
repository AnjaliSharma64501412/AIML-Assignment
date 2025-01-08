n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Numbers from 1 to", n, ":")
    for i in range(1, n + 1):
        print(i)

    total_sum = 0
    i = 1
    while i <= n:
        total_sum += i
        i += 1

    print("The sum of numbers from 1 to", n, "is:", total_sum)
