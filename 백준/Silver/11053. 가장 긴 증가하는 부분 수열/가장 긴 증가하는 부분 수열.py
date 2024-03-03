import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.insert(0, 0)

dp = [0]*(n+1)
dp[1] = 1

for idx in range(2, n+1):
    target = li[idx]
    tmp_li = []
    for tmp_idx, i in enumerate(li[:idx]):
        if target > i:
            tmp_li.append(dp[tmp_idx] + 1)
        else:
            tmp_li.append(1)
    dp[idx] = max(tmp_li)

print(max(dp))