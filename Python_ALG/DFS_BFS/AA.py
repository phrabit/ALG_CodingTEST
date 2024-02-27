import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def BFS(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        now = queue.popleft()

        for i in range(8):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]

            if 0<=xx<n and 0<=yy<n:
                if li[xx][yy] == 1:
                    queue.append((xx,yy))
                    li[xx][yy] = 0


    

if __name__ == "__main__":
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if li[i][j] == 1:
                cnt += 1
                BFS(i, j)

print(cnt)