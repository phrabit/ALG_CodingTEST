import sys
from collections import deque
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())

dp = [0]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    src, dst = map(int, input().split())

    graph[src][dst] = 1
    dp[dst] = dp[dst] + 1

queue = deque()
for idx, val in enumerate(dp):
    if val == 0 and idx>0:
        queue.append(idx)
        dp[idx] = 99999

while queue:
    now = queue.popleft()
    print(now, end=" ")

    for i in range(1, n+1):
        if graph[now][i] > 0:
            dp[i] = dp[i] - 1
     
    for i in range(1, n+1):
        if dp[i] == 0:
            queue.append(i)
            dp[i] = 99999
