import sys
input = sys.stdin.readline


n,m = map(int, (input().split()))

def Count(len):
    cnt = 0
    for i in li:
        cnt += (i//len)
    return cnt

li = []
res = 0

for _ in range(n):
    num = int(input())
    li.append(num)

lt = 1
rt = max(li)

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
