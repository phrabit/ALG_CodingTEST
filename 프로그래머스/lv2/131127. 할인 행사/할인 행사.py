from collections import Counter
# discount정보를 Counter로..!
# market = Counter(discount)
    
    
    

def solution(want, number, discount):
    
    cnt = 0
    
    # want와 number를 합하여 dictionary로 만든것
    my_want = dict(zip(want, number))
    my_want = sorted(my_want.items(), key=lambda x:x[0])
    
    for i in range(len(discount) - sum(number) + 1):
        tmp_li = discount[i:i+10]
        market = Counter(tmp_li)
        market = sorted(market.items(), key=lambda x:x[0])
        
        if my_want == market:
            cnt += 1
    
    return cnt