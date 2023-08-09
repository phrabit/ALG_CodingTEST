# Greedy 알고리즘을 어떻게 사용할 것인가가 핵심인 문제. 보트를 가장 적은 횟수로 사람들을 이동시키려면 제일 무거운 사람, 제일 가벼운 사람을 같이 묶어서 처리해야한다는 게 핵심 아이디어다.

# 1. people 리스트를 덱으로 만든 후 내림차순 정렬

# 2. 무거운 사람(왼쪽)과 가벼운 사람(오른쪽)을 인덱스로 매칭

# 3. 합이 보트 무게보다 가벼우면 둘 빼냄

# 4. 보트 무게보다 무거우면 무거운 사람만 빼냄

from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    cnt = 0
    
    while len(people)>1:
        if people[0]+people[-1]<=limit:
            cnt+=1
            people.popleft()
            people.pop()
        else:
            cnt+=1
            people.popleft()
    
    if people:
        cnt += 1
    
    return cnt
            
    
    