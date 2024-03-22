# 상태트리 구상과 스택프레임 구조 구상하기!!
# 이건 곧잘 생각해냄. Cut edge까지!!

def DFS(idx, sum):
    if sum > total//2:
        return
    if idx == n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(idx+1, sum+li[idx])
        DFS(idx+1, sum)
        

if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split()))
    total = sum(li)

    DFS(0, 0)
    print("NO")
