def solution(s):
    res = ""
    li = sorted([ord(i) for i in s], reverse=True)
    
    for i in li:
        res += chr(i)
    
    return res
    