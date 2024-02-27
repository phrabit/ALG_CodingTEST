from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x,y,lim):

    ck[x][y] = 1

    queue = deque()
    queue.append((x,y))

    while queue:
        now = queue.popleft()

        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]

            if 0<=xx<n and 0<=yy<n:
                if li[xx][yy] > lim and ck[xx][yy] == 0:
                    ck[xx][yy] = 1
                    queue.append((xx,yy))


if __name__ == "__main__":
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]

    max = 0
    cnt = 0
    cnt_li = []

    for row in li:
        for i in row:
            if i>max:
                max = i

    for limit in range(max):
        ck = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if li[i][j] > limit and ck[i][j] == 0:
                    cnt+=1
                    BFS(i,j, limit)
        
        cnt_li.append(cnt)
                   
print(sorted(cnt_li)[-1])