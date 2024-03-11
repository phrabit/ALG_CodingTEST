import sys
#sys.stdin=open("input.txt", "r")

n, limit = map(int, input().split())

score_li = []
time_li = []
dp = [0]*(limit+1)

for _ in range(n):
    score, time = map(int, input().split())
    score_li.append(score)
    time_li.append(time)

for i in range(n):
    for j in range(limit, time_li[i]-1, -1):
        dp[j] = max( dp[j], dp[j-time_li[i]]+score_li[i] )

print(dp[limit])
