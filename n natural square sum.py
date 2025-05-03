n = int(input("Enter the value of n: "))

sum = 0
for i in range(1, n + 1):
    sum = sum + i * i

print("Sum of squares of first", n, "natural numbers is:", sum)
