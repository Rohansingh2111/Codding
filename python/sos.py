def series_sum(n):
     total = 0
     series = ""
     for i in range(1, n + 1):
         total += 1 / i
         if i == 1:
             series += "1"
         else:
             series += " + 1/" + str(i)
     return total, series

# # Test the function
n = int(input("Enter the value of n: "))
result, series = series_sum(n)
print("Series:", series)
print("Sum of the series is: {:.2f}".format(result))



