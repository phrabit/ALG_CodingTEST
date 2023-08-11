def solution(sizes):
    big_li = []
    small_li = []
    
    for i in sizes:
        big_li.append(max(i))
        small_li.append(min(i))
        
    bignum = sorted(big_li)[-1]
    smallnum = sorted(small_li)[-1]
    
    return bignum*smallnum