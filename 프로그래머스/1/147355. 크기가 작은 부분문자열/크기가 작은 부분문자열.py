def solution(t, p):
    
    length = (len(t) - len(p)) + 1
    cnt = 0
    
    for i in range(0, length):
        part = int(t[i:i+len(p)])
        
        if part <= int(p):
            cnt += 1
    
    return cnt
    
    
            