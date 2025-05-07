def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Example input
n = int(input("ENter a number :"))
print("Number of ways to climb:", climb_stairs(n))
