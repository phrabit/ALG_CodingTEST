def DFS(n, cnt):
    if n == b:
        return cnt
    if n > b:
        return float('inf')  # b보다 커지면 이 경로는 무효화
    
    return min(DFS(n*2, cnt+1), DFS(int(str(n)+'1'), cnt+1))

if __name__ == "__main__":
    a, b = map(int, input().split())

    result = DFS(a, 1)
    print(result if result != float('inf') else -1) 