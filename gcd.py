a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
while b!=0:
    temp=b
    b=a%b
    a=temp
gcd=a
print("GCD =",gcd)
