def swap_without_temp(a,b):
    a,b=b,a
    return a,b
x=int(input("Enter the 1st number :"))
y=int(input("Enter the 2nd number :"))

x2,y2=swap_without_temp(x,y)
print("Swapping without temporary value \n","x2 =",x2,"y2 =",y2)

def swap_without_temp(a,b,c):
    a,b,c=c,a,b
    return a,b,c
x=int(input("Enter the 1st number :"))
y=int(input("Enter the 2nd number :"))
z=int(input("Enter the 3rd number :"))

x1,y1,z1=swap_without_temp(x,y,z)
print("Swapping without temporary value \n","x1 =",x1,"y1 =",y1,"z1 =",z1)

import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
x1,y1=1,2
x2,y2=3,4
distance=distance(x1,y1,x2,y2)
print(distance)
