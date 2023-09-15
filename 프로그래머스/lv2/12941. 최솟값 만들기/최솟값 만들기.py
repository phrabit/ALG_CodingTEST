def solution(A,B):
    answer = 0

    new_A = sorted(A)
    new_B = sorted(B, reverse=True)
    
    for a,b in zip(new_A, new_B):
        answer += (a*b)

    return answer