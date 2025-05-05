def swap_with_temp(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def swap_without_temp(a,b):
    a,b=b,a
    return a,b
x=int(input("Enter the 1st number :"))
y=int(input("Enter the 2nd number :"))

x1,y1=swap_with_temp(x,y)
print("Swapping with temporary value \n","x1 =",x1,"y1 =",y1)

x2,y2=swap_without_temp(x,y)
print("Swapping without temporary value \n","x2 =",x2,"y2 =",y2)
