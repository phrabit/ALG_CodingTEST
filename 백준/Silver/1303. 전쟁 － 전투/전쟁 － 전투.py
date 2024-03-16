from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y): 
    global cnt

    queue = deque()
    queue.append((x,y))
    ck[x][y] = True

    while queue:
        now = queue.popleft()
        
        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]

            if 0<=xx<m and 0<=yy<n:
                if li[now[0]][now[1]] == li[xx][yy] and not ck[xx][yy]:
                    queue.append((xx, yy))
                    ck[xx][yy] = True
                    cnt += 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    li = [['X']*n for _ in range(m)]
    ck = [[False]*n for _ in range(m)]
    white_li = []
    blue_li = []

    for i in range(m):
        soldiers = input()
        
        for j in range(n):
            li[i][j] = soldiers[j]

    for x in range(m):
        for y in range(n):
            if li[x][y] == "W" and not ck[x][y]:
                cnt = 1
                BFS(x,y)
                white_li.append(cnt)

    for x in range(m):
        for y in range(n):
            if li[x][y] == "B" and not ck[x][y]:
                cnt = 1
                BFS(x,y)
                blue_li.append(cnt)

    white_score, blue_score = 0, 0
    for i in white_li:
        white_score += i**2
    
    for i in blue_li:
        blue_score += i**2
    
    print(white_score, blue_score)
