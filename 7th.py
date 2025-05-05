import math
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def find_largest(numbers):
    return max(numbers)
def area_of_shape(shape):
    if shape == 'circle':
        radius = float(input("Enter radius: "))
        return math.pi * radius * radius
    elif shape == 'rectangle':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        return length * width
    elif shape == 'triangle':
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        return 0.5 * base * height
    else:
        return None


print("1. Factorial")
print("2. Largest number in list")
print("3. Area of shape")
choice = int(input("Enter your choice: "))

if choice == 1:
    num = int(input("Enter a number: "))
    print("Factorial =", factorial(num))

elif choice == 2:
    count = int(input("How many numbers? "))
    numbers = []
    for i in range(count):
        val = float(input(f"Enter number {i+1}: "))
        numbers.append(val)
    print("Largest number =", find_largest(numbers))

elif choice == 3:
    shape = input("Enter shape (circle / rectangle / triangle): ").lower()
    area = area_of_shape(shape)
    if area is not None:
        print(f"Area of {shape} = {area:.2f}")
    else:
        print("Invalid shape.")

else:
    print("Invalid choice.")
