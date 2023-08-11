def solution(sizes):
    big_li = []
    small_li = []
    
    for i in sizes:
        if i[0] > i[1]:
            big_li.append(i[0])
            small_li.append(i[1])
        else:
            big_li.append(i[1])
            small_li.append(i[0])
    
    bignum = sorted(big_li)[-1]
    smallnum = sorted(small_li)[-1]
    
    return bignum*smallnum