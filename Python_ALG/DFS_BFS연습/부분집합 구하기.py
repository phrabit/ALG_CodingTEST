# 상태트리와 스택프레임 구조만 잘 구상하자!!

# DFS 재귀호출을 했을 때, 다시 돌아올 때 몇번째 줄로 되돌아오는지,
# 그때의 변수는 뭔지 등 스택프레임 구조를 잘 기억해야 함!!

def DFS(x):
    if x==n+1:
        for i in range(1, n+1):
            if li[i] == 1:
                print(i, end=" ")
        print()
    else:
        li[x] = 1
        DFS(x+1)
        li[x] = 0
        DFS(x+1)
        

if __name__ == "__main__":
    n = int(input())
    li = [0]*(n+1)

    DFS(1)
