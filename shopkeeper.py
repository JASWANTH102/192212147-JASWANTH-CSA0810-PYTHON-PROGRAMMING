def cal_bill(items):
    total=0
    for item in items:
        total+=item['price']*item['quantity']
    return total

items=[
    {"name": "apple","price":10,"quantity":5},
    {"name": "banana","price":4,"quantity":12},
    {"name": "milk","price":30,"quantity":2},
    {"name": "bread","price":25,"quantity":1}
]
total_bill=cal_bill(items)
print("Total bill =",total_bill)
