import sys
#sys.stdin=open("input.txt", "r")

dx = [0, 0, -1]
dy = [-1, 1, 0]

def DFS(x, y):
    if x == 0:
        print(y)
        sys.exit(0)
    
    for i in range(3):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0<=xx<10 and 0<=yy<10:
            if li[xx][yy] == 1 and ck[xx][yy] == 0:
                ck[xx][yy] = 1
                DFS(xx, yy)

if __name__ == "__main__":
    li = [list(map(int, input().split())) for _ in range(10)]
    ck = [[0]*10 for _ in range(10)]

    x = 0
    y = 0

    for i in range(10):
        for j in range(10):
            if li[i][j] == 2:
                ck[i][j] = 1
                x, y = i, j
                break

    DFS(x, y)