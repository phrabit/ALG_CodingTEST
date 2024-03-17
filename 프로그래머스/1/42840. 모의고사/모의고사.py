def solution(answers):
    length = len(answers)
    a_cnt, b_cnt, c_cnt = 0, 0, 0
    
    a = ([1,2,3,4,5]*2000)[:length]
    b = ([2,1,2,3,2,4,2,5]*1250)[:length]
    c = ([3,3,1,1,2,2,4,4,5,5]*1000)[:length]
    
    for idx in range(length):
        if answers[idx] == a[idx]:
            a_cnt += 1
    
    for idx in range(length):
        if answers[idx] == b[idx]:
            b_cnt += 1

    for idx in range(length):
        if answers[idx] == c[idx]:
            c_cnt += 1
            
    res = [a_cnt, b_cnt, c_cnt]
    tmp = []
    
    for idx, i in enumerate(res):
        if max(res) == i:
            tmp.append(idx+1)
            
    return tmp
        