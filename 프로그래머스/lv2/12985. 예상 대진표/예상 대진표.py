def solution(n,a,b):
    cnt = 1
    
    while True:            
        a = (a//2) + (a%2)
        b = (b//2) + (b%2)
        
        if a==b:
            break;
        
        cnt+=1
    
    return cnt
        