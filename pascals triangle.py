rows = int(input("Enter number of rows: "))

for i in range(rows):
    # Print spaces for alignment
    for j in range(rows - i - 1):
        print(" ", end=" ")

    # Calculate and print values in row i
    num = 1
    for k in range(i + 1):
        print(num, end="   ")
        # Compute next number using formula:
        # C(i, k+1) = C(i, k) * (i-k)/(k+1)
        num = num * (i - k) // (k + 1)

    print()  # Move to the next line
