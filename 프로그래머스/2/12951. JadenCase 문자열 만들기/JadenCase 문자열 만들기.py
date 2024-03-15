def solution(s):
    
    idx_li = []
    li = s.split()
    res = []
    result = []
    
    # 공백있는 인덱스 위치 찾기
    for idx, i in enumerate(s):
        if i == " ":
            idx_li.append(idx)

    # 토큰 별 JadenCase 문자열 만들기
    for i in li:
        i = i[0].capitalize() + i[1:].lower()
        res.append(i)
    
    # Jadencase와 공백 문자열 합치기
    for i in res:
        for j in i:
            result += j
    
    for i in idx_li:
        result.insert(i, " ")
    
    tmp = "".join(result)
    return tmp