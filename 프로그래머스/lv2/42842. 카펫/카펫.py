def solution(brown, yellow):
    answer = []
    
    tmp = brown+yellow
    for i in range(1, tmp+1):
        target = tmp//i
        if brown == (i*2)+((target-2)*2):
            if i>=target:
                return [i, target]
