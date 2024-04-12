def pow(x, n):
    return x ** n

# Get input from the user
x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

# Calculate the result and print it
result = pow(x, n)
print(f"{x} raised to the power of {n} is:", result)

