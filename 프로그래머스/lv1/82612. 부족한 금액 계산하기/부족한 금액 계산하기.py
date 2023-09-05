def solution(price, money, count):
    sum = 0
    for i in range(1, count+1):
        sum += i*price
    
    result = sum - money
    
    return result if result>0 else 0