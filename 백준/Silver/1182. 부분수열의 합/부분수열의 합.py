import sys
input = sys.stdin.readline

def DFS(idx, sum):
    global cnt

    if idx == n:
        if target == sum:
            cnt += 1
    else:
        DFS(idx+1, sum+li[idx])
        DFS(idx+1, sum)


    return cnt;

if __name__ == "__main__":
    n, target = map(int, input().split())
    li = list(map(int, input().split()))

    total = sum(li)
    cnt = 0
    res = DFS(0, 0)

    if target==0 and res>0:
        print(res - 1)
    else:
        print(res)