def solution(s):
    
    # <제일 쉬운 코드>
    # return "".join(s)
    
    res = ""
    li = sorted([ord(i) for i in s], reverse=True)
    
    for i in li:
        res += chr(i)
    
    return res
    