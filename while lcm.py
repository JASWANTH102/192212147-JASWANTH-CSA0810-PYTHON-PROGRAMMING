a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


lcm = a if a > b else b

while True:
    if lcm % a == 0 and lcm % b == 0:
        print("LCM of", a, "and", b, "is:", lcm)
        break
    lcm += 1
