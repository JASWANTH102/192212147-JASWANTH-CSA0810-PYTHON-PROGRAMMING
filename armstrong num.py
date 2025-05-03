num=int(input("Enter a number : "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**len(str(num))
    temp//=10
if sum==num:
    print("The number is armstrong number")
else:
    print("The number is not armstrong number")
