def solution(num):
    cnt = 0
    flag = True
    
    while num!=1:
        
        if cnt>500:
            flag = False
            break

        if num%2==0:
            num //= 2
        else:
            num = (num*3) + 1
        
        cnt += 1

    return cnt if flag else -1 