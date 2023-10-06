# def solution(citations):
#     answer = 0
    
#     li = []
#     citation = sorted(citations)
    
#     for i in range(len(citation)):
#         over_num = len(citation[i:]) # citation[i]번 이상 인용된 논문의 수
#         under_num = len(citation[:i+1])
        
#         if over_num==under_num:
#             return over_num



def solution(citations):
    result = 0
    
    li = [i for i in range(min(citations), max(citations)+1)] #인덱싱을 위한 리스트
    
    for i in li:
        over_num = 0
        under_num = 0
        for j in sorted(citations):
            if i==j:
                over_num+=1
                under_num+=1
            elif j>i:
                over_num += 1
            elif j<i:
                under_num += 1
        
        #print(i, over_num, under_num)
        if i==over_num==under_num:
            return i
        
        
def solution(citations):
    citations.sort(reverse=True)  # citations 배열을 내림차순으로 정렬

    h_index = 0  # H-Index 초기값

    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index
    
    