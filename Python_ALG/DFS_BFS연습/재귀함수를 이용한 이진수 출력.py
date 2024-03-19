def DFS(n):
    global res

    if n==0:
        return
    else:
        DFS(n//2)
        print(n%2, end="")
        


if __name__ == "__main__":
    n = int(input())
    res = []

    DFS(n)
