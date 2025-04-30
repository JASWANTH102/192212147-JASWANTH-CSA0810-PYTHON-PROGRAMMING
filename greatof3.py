a=int(input("Enter the value of a :"))
b=int(input("Enter the value of a :"))
c=int(input("Enter the value of a :"))
if(a>b):
    if(a>c):
        print("the greatest number is ",a)
    else:
        print("The greatest number is ",c)
else:
    if(b>c):
        print("The greatest number is ",b)
    else:
        print("The greatest number is ",c)
