# 나의 1차 풀이 -> 완전탐색(brute force)
# 시간초과 발생

def solution(elements):
    
    sum_li = [] # 연속 부분 수열 합을 넣을 리스트
    
    db_elements = elements * 2 #현재 리스트를 하나 더 이어붙임.
    
    # 완전 탐색으로 모든 경우의 수를 다 고려하고, 중복되지 않으면 sum_li에 추가
    for i in range(0, len(elements)): 
        for j in range(0, len(elements)):
            tmp = sum(db_elements[j:i+j+1])

            sum_li.append(tmp)
    
    return len(set(sum_li))




