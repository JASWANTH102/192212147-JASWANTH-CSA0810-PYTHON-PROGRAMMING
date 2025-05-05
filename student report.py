def student(marks):
    if marks>=50:
        return "Passed"
    else:
        return "Failed"
marks=int(input("Enter the marks of student :"))
result=student(marks)
print("Result =",result)
