from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y):
    global cnt
    queue = deque()
    queue.append((x,y))

    while queue:
        now = queue.popleft()

        for idx in range(4):
            xx = now[0] + dx[idx]
            yy = now[1] + dy[idx]

            if 0<=xx<n and 0<=yy<m:
                if li[xx][yy] == 1:
                    li[xx][yy] = 0
                    queue.append((xx,yy))
                    cnt += 1
    

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    li = [[0]*m for _ in range(n)]
    cnt_li = []

    for _ in range(k):
        x, y = map(int, input().split())
        li[x-1][y-1] = 1

    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                cnt = 0
                BFS(i, j)
                cnt_li.append(cnt)
    
    
    print(max(cnt_li))