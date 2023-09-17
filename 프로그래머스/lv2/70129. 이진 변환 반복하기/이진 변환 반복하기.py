# 나의 1차 풀이 -> 리스트로 풀기 실패
# def solution(s):
    
#     change_cnt = 0 # 변환횟수
#     zero_cnt = 0 # 제거된 0의 개수
    
#     #리스트로 풀자
#     s_list = [i for i in s]
    
#     while True:
#         if len(s_list) == 1:
#             break;
        
#         for i in s_list:
#             if i == '0':
#                 s_list.remove(i)
#                 zero_cnt+=1
        
#         tmp = bin(len(s_list))[2:]
#         s_list = [i for i in tmp]
#         change_cnt += 1
    
#     return [change_cnt, zero_cnt]


def solution(s):
    change_cnt = 0 # 변환횟수
    zero_cnt = 0 # 제거된 0의 개수
    
    while True:
        
        if len(s)==1:
            break;
        
        zero_cnt += s.count('0')
        tmp = '1'*s.count('1')
        s = bin(len(tmp))[2:]
        change_cnt+=1
        
    
    return [change_cnt, zero_cnt]
    