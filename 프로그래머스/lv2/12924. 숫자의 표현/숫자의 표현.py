# 첫번째 풀이 : 시간초과
# def solution(n):
    
#     li = [i for i in range(1, n+1)]
    
#     answer_li = []
#     answer = 0
    
#     for i in range(2, len(li)):
#         for j in range(n):
#             if sum(li[j:j+i]) == n:
#                 answer_li.append(li[j:j+i])
    
#     for i in answer_li:
#         if len(i)!=1:
#             answer += 1
    
#     return answer +1 

            
# 두번째 풀이
# 내가 하려했던 로직은 같다... 단, 리스트로 구현하지 않았을 뿐.
def solution(num):
    answer = 0
    for x in range(1,num+1):
        sum = 0
        for y in range(x, num+1):
            sum += y
            if sum == num:
                answer += 1
                break
            elif sum > num:
                break

    return answer
