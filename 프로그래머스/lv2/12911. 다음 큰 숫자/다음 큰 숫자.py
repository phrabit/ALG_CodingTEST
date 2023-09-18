def solution(n):
    answer = 0
    tmp = n

    while True:
        tmp += 1
        
        if bin(tmp)[2:].count('1') == bin(n)[2:].count('1') :
            return tmp