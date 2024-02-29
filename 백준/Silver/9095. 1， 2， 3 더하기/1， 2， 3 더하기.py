import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    li = [0] * (num + 1)

    for idx in range(1, num+1):
        if idx == 1:
            li[idx] = 1
        elif idx == 2:
            li[idx] = 2
        elif idx == 3:
            li[idx] = 4
        else:
            li[idx] = li[idx-3] + li[idx-2] + li[idx-1]

    print(li[num])