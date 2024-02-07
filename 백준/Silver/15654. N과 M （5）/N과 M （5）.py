def DFS(L):
    if L==m:
        if len(set(res)) == len(res):
            for i in res:
                print(i, end=" ")
            print()
    else:
        for i in range(0, n):
            res[L] = li[i]
            DFS(L+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    li = sorted(list(map(int, input().split())))

    res = [0]*m
    DFS(0)