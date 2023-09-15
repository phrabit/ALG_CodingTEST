def solution(A,B):
    answer = 0

    new_A = sorted(A)
    new_B = sorted(B, reverse=True)
    
    for i in range(len(A)):
        answer += (new_A[i]*new_B[i])

    return answer