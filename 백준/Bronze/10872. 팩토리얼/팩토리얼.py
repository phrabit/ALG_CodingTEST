n = int(input())
result = 1
if n==0:
    print("1")
else:
    for i in range(1, n+1):
        result *= i
    print(result)