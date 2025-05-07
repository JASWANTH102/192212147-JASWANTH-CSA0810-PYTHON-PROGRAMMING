import array
l=[1,2,3,4,5]
sum=0
a=array.array("i",[])
a.fromlist(l)
print(a)
for i in a:
    sum+=i
print(sum)
