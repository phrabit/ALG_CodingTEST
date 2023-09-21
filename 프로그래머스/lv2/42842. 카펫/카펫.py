def solution(brown, yellow):
    answer = []
    
    sum = brown+yellow
    
    for i in range(sum-1, 1, -1):
        if sum%i == 0:
            j = sum//i
            if j > i:
                break;
            elif (i-2)*(j-2) == yellow:
                answer = [i,j]
                
    return answer