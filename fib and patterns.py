# Fibonacci Series
def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# Number Pattern (Right-angled Triangle)
def number_pattern(rows):
    print("Number Pattern:")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Pyramid Pattern
def pyramid_pattern(rows):
    print("Pyramid Pattern:")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end='')  # Spaces
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Main menu
print("1. Fibonacci Series")
print("2. Number Pattern")
print("3. Pyramid Pattern")
choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    n = int(input("Enter number of terms: "))
    fibonacci_series(n)
elif choice == 2:
    rows = int(input("Enter number of rows: "))
    number_pattern(rows)
elif choice == 3:
    rows = int(input("Enter number of rows: "))
    pyramid_pattern(rows)
else:
    print("Invalid choice.")
