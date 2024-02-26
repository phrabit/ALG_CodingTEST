from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x,y):
    global cnt
    cnt += 1
    li[x][y] = 0

    queue = deque()
    queue.append((x,y))

    while queue:
        now = queue.popleft()

        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]

            if 0<=xx<n and 0<=yy<n:
                if li[xx][yy] == 1:
                    li[xx][yy] = 0
                    queue.append((xx,yy))
                    cnt += 1

    

if __name__ == "__main__":
    n = int(input())
    li = []
    cnt_li = []

    for i in range(n):
        row = input()
        tmp = list()
        for j in row:
            tmp.append(int(j))
        li.append(tmp)

    for x in range(n):
        for y in range(n):
            if li[x][y] == 1:
                cnt = 0
                BFS(x,y)
                cnt_li.append(cnt)
    
    num = len(cnt_li)

    print(num)
    for i in sorted(cnt_li):
        print(i)