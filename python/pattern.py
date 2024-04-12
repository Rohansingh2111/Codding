rows = 5 # Define the number of rows for the pattern
# Outer loop to iterate through each row
for i in range(10, rows + 10):
    # Inner loop to print numbers from 1 to i
    for j in range(10, i + 10):
        print(j, end=" ")
    print()  # Move to the next line after printing each row