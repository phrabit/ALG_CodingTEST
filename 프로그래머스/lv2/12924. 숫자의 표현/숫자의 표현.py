def solution(n):
    cnt = 0
    
    for i in range(1, n):
        sum = 0
        for j in range(i, n):
            sum += j
            if sum == n:
                cnt+=1
                break;
            elif sum > n:
                break;
    
    return cnt+1