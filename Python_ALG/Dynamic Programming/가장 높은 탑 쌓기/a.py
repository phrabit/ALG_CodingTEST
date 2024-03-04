n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li = sorted(li, key=lambda x:x[0], reverse=True)

dp = [0]*(n)
dp[0] = li[0][1]

for i in range(1, n):
    area = li[i][0]
    height = li[i][1]
    weight = li[i][2]

    max = 0

    for j in range(i-1, -1, -1):
        prev_area = li[j][0]
        prev_height = li[j][1]
        prev_weight = li[j][2]

        if (area<prev_area) and (weight<prev_weight):
            tmp = dp[j] + height
            if tmp > max:
                max = tmp
    
    dp[i] = height if max==0 else max


dp.sort()
print(dp[-1])
