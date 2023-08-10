from itertools import combinations

def solution(numbers):
    li = set(combinations(numbers,2))
    answer = []
    for i in li:
        answer.append(sum(i))
    
    return (sorted(list(set(answer))))