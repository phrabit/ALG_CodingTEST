# 내 풀이는, 모든 경우의 수를 다 나눴음.
# def solution(n,a,b):
#     cnt = 0
    
#     while True:
#         li = []
#         if a%2==0 and b%2==0:
#             a= a//2
#             b= b//2
#             li = sorted([a,b])
#             if li[1]-li[0] == 1:
#                 cnt+=1
#                 break;
#             else:
#                 cnt+=1
#         elif a%2!=0 and b%2!=0:
#             a = (a+1)//2
#             b = (b+1)//2
#             li = sorted([a,b])
#             if li[1]-li[0] == 1:
#                 cnt+=1
#                 break;
#             else:
#                 cnt+=1
#         elif a%2!=0 and b%2==0:
#             a = (a+1)//2
#             b= b//2
#             li = sorted([a,b])
#             if li[1]-li[0] == 1:
#                 cnt+=1
#                 break;
#             elif li[0]-li[1] == 0:
#                 break;
#             else:
#                 cnt+=1
#         elif a%2==0 and b%2!=0:
#             b= (b+1)//2
#             a = a//2
#             li = sorted([a,b])
#             if li[1]-li[0] == 1:
#                 cnt+=1
#                 break;
#             elif li[0]-li[1] == 0:
#                 break;
#             else:
#                 cnt+=1

#     return cnt+1

def solution(n,a,b): 
	answer = 0
	while a != b: 
		answer += 1
        # 1을 더해서 2로 나누었을 때, 자리수를 맞춰줌
        # 예) 1, 2의 경우는 2, 3으로 해서 나눴을때 몫이 1이 되도록
		a, b = (a+1)//2, (b+1)//2
	return answer