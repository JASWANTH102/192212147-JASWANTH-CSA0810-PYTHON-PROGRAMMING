s = input("Enter a string: ")
reversed_string = ""
length = 0
for char in s:
    length += 1
i = length - 1
while i >= 0:
    reversed_string += s[i]
    i -= 1
print("Reversed string:", reversed_string)
