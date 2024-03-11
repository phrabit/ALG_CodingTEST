import sys
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())

dp = [[99999]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for _ in range(m):
    src, dst, dis = map(int, input().split())
    dp[src-1][dst-1] = dis

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            
for i in range(n):
    for j in range(n):
        if dp[i][j] == 99999:
            print('M', end=" ")
        else:
            print(dp[i][j], end=" ")
    print()
