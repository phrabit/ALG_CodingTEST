def solution(s):
    
    result = ""
    tmp = ""
    
    hash = {"zero":0,
           "one":1,
           "two":2,
           "three":3,
           "four":4,
           "five":5,
           "six":6,
           "seven":7,
           "eight":8,
           "nine":9}
    
    for i in s:
        if i.isdigit():
            result += i
            continue
        
        tmp += i
        
        if tmp in hash.keys():
            #print(tmp, hash[tmp])
            result += str(hash[tmp])
            tmp = ""
            continue
        
    return int(result)