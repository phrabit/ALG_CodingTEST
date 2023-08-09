def solution(A,B):
    sum = 0

    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for i in range(len(A)):
        sum += (A[i]*B[i])
    return sum