def sum(a,b):
   sum=a+b
   return sum

def avg(sum):
   avg=sum/2
   return avg

a=int(input("enter a:"))
b=int(input("enter b:"))

sum=sum(a,b)
avg=avg(sum)

print("the avg is",avg)
