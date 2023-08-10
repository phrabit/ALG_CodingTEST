# <나의 코드>
# 한가지 경우에 대해서만 시간초과 나고, 나머진 다 맞음 (96/100)

# def solution(n):
#     ans = 0
    
#     while n>1:
#         if n%2==0:
#             n = n//2
#         else:
#             n -= 1
#             n = n//2
#             ans += 1   

#     return ans+1



# <정답 코드>
def solution(N):
    answer = 0
    while N > 0:
        answer += N % 2
        N //= 2
    return answer