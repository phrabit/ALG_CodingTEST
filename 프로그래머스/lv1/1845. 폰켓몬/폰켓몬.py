# <나의 첫번째 풀이> -> 시간 초과

# from itertools import combinations

# def solution(nums):
    
#     li = list(combinations(nums, len(nums)//2))
#     li = [len(set((i))) for i in li]
    
#     return max(li)


def solution(nums):
    stack = []
    num = list(set(nums))
    
    for i in num:
        stack.append(i)
        
        if len(stack)==(len(nums)//2):
            break;
        elif i in stack:
            continue;
    
    return len(stack)
