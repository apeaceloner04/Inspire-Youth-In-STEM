def factorial(n):
    """Returns the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Taking input from user
num = int(input("Enter a number: "))

# Calling the factorial function and printing the result
print("Factorial of", num, "is", factorial(num))


#write a program to calculate simple intrest 
# Taking input from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculating simple interest
interest = (principal * rate * time) / 100

# Printing the result
print("Simple interest for the given principal amount, rate of interest, and time period is:", interest)