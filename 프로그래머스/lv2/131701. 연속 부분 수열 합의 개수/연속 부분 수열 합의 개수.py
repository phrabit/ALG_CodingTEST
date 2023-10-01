# 나의 1차 풀이 -> 완전탐색(brute force)
# : 테스트3부터 시간초과 발생...

def solution(elements):
    
    sum_li = [] # 연속 부분 수열 합을 넣을 리스트
    
    db_elements = elements * 2 #현재 리스트를 하나 더 이어붙임.
    
    # 완전 탐색으로 모든 경우의 수를 다 고려하고, 중복되지 않으면 sum_li에 추가
    for i in range(0, len(elements)): 
        for j in range(1, len(elements)+1):
            tmp = sum(db_elements[i:i+j])

            if tmp not in sum_li:
                sum_li.append(tmp)
    
    return len(sum_li)
        
    
def solution(elements):
    sum_li = set()

    db_elements = elements * 2
    
    for i in range(0, len(elements)):
        for j in range(0, len(elements)):
            sum_li.add(sum(db_elements[j:j+i+1]))
    return len(sum_li)