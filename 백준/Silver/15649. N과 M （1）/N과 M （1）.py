def DFS(L):
    if L == m:
        for i in res:
            print(i, end=" ")
        print()
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                res[L] = i
                DFS(L+1)
                check[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())

    check = [0]*(n+1)
    res = [0]*m

    DFS(0)
