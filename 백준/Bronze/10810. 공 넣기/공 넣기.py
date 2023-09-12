n, m = map(int, input().split())

li = [0 for i in range(n)] #초기화

for _ in range(m):
    i,j,k = map(int, input().split())
    for idx in range(i-1,j):
        li[idx] = k
    #print(li)

for i in li:
    print(i, end=" ")