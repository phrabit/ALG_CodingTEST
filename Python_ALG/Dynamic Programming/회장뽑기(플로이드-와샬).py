import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
dp = [[9999]*(n+1) for _ in range(n+1)]
res = []

for i in range(n+1):
    dp[0][i] = 0
    dp[i][0] = 0
    dp[i][i] = 0

while True:
    p1, p2 = map(int, input().split())

    if p1==-1 and p2==-1:
        break

    dp[p1][p2], dp[p2][p1] = 1,1 

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])


for i in range(1, n+1):
    max = 0
    for j in range(1, n+1):
        if dp[i][j] > max:
            max = dp[i][j]
    res.append(max)


president_score = min(res)
cnt = 0
for i in res:
    if i==president_score:
        cnt+=1

print(president_score, cnt)

for idx, score in enumerate(res):
    if score == president_score:
        print(idx+1, end=" ")
