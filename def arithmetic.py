def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Error: Division by zero"
    return a/b

def calculate(a,b,op):
    if op=="+":
        return add(a,b)
    elif op=="-":
        return subtract(a,b)
    elif op=="*":
        return mul(a,b)
    elif op=="/":
        return div(a,b)
    else:
        return "Error: enter valid operator"

n1=int(input("Enter 1st number :"))
n2=int(input("Enter 2nd number :"))
operator=input("Enter an operator + - * / :\n")

result=calculate(n1,n2,operator)
print("Result =",result)

