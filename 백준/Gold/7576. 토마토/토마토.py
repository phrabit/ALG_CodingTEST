from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(m)]
day_li = [[0]*n for _ in range(m)]

queue = deque()

for i in range(m):
    for j in range(n):
        if li[i][j] == 1:
            queue.append((i,j))
            
while queue:
    now = queue.popleft()
    
    for i in range(4):
        xx = now[0] + dx[i]
        yy = now[1] + dy[i]
        
        if 0<=xx<m and 0<=yy<n:
            if li[xx][yy] == 0:
                day_li[xx][yy] = day_li[now[0]][now[1]] + 1
                li[xx][yy] = 1
                queue.append((xx,yy))
                
flag = 1
for i in range(m):
    for j in range(n):
        if li[i][j] == 0:
            flag = 0
            
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if day_li[i][j] > result:
                result = day_li[i][j]
                
    print(result)
else:
    print(-1)
            