positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    
    if num == -1:
        break
    elif num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1

if positive_count > 0:
    pos_avg = round(positive_sum / positive_count, 2)
else:
    pos_avg = 0

if negative_count > 0:
    neg_avg = round(negative_sum / negative_count, 2)
else:
    neg_avg = 0

print("Average of positive numbers:", pos_avg)
print("Average of negative numbers:", neg_avg)
