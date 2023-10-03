from collections import deque

def solution(s):
    cnt = 0
    
    # 덱으로 구현 (편리함 때문)
    stack = deque(s)
    
    for i in range(len(s)):
        
        # 맨 왼쪽에 원소를 맨 뒤에 붙이기
        stack.append(stack.popleft())
        
        # 1칸씩 회전된 스택이 '올바른 괄호 문자열'인지 확인하는 함수 적용하기
        if isStack(stack):
            cnt += 1
    
    return cnt
        
    
def isStack(stack):
    
    tmp = []
    
    for char in stack:
        if char in ['(', '{', '[']:
            tmp.append(char)
        elif char in [')', '}', ']']:
            if not tmp: # tmp가 비어있을 때
                return False
            
            top = tmp.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return False
    
    return not tmp
            
    