n=int(input("Enter the value of n : "))
rev=0
while(n>0):
    a=n%10
    rev=10*rev+a
    n=n//10
print(rev)
