def solution(price, money, count):
    payment = 0
    
    for i in range(1, count+1):
        tmp = i*price
        payment += tmp
    
    result = payment - money
    
    return result if result > 0 else 0