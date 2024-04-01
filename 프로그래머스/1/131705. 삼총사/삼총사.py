from itertools import combinations

def solution(number):
    cnt = 0
    com = list(combinations(number,3))
    for i in com:
        if sum(i) == 0:
            cnt += 1
    
    return cnt