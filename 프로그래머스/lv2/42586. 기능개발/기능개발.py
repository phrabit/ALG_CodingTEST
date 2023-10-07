def solution(progresses, speeds):
    li = []
    result = []
    cnt = 1
    
    for i,j in zip(progresses, speeds):
        num = (100-i)//j if (100-i)%j==0 else ((100-i)//j) + 1
        li.append(num)

    print(li)
    max = li[0]
    
    for i in range(1, len(li)):        
        if max >= li[i]:
            cnt += 1 
            continue;
        else:
            max = li[i]
            result.append(cnt)
            cnt = 1
    
    result.append(cnt)
            
    return result
            
        
