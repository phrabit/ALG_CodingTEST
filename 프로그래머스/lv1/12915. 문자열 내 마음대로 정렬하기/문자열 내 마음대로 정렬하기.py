# 람다 조건 정렬하기

def solution(strings, n):
    
    strings = sorted(strings)
    answer = sorted(strings, key= lambda x: x[n])
    
    return answer