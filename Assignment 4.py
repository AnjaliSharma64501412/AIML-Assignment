def sum_of_even_numbers(n):
    if n < 1:
        return 0

    max_even = n if n % 2 == 0 else n - 1
    num_of_evens = max_even // 2
    return num_of_evens * (num_of_evens + 1)

try:
    n = int(input("Enter a positive integer: "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        result = sum_of_even_numbers(n)
        print(f"The sum of all even numbers between 1 and {n} is: {result}")
except ValueError:
    print("Invalid input! Please enter a valid positive integer.")
