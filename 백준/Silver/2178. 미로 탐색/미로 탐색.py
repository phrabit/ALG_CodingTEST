from collections import deque

n,m = map(int, input().split())
li = []
for i in range(n):
    nums = input()
    tmp = []
    for num in nums:
        tmp.append(int(num))
    li.append(tmp)

ck = [[0]*m for _ in range(n)]
dis = [[0]*m for _ in range(n)]
queue = deque()

ck[0][0] = 1
queue.append((0,0))

while queue:
    now = queue.popleft()

    for next in ((now[0]-1, now[1]), (now[0], now[1]+1), (now[0]+1, now[1]), (now[0], now[1]-1)):
        x, y = next[0], next[1]
        if 0<=x<=n-1 and 0<=y<=m-1:
            if li[x][y] == 1 and ck[x][y]==0:
                ck[x][y] += 1
                dis[x][y] = dis[now[0]][now[1]] + 1

                queue.append((x,y))

print(dis[n-1][m-1] + 1)