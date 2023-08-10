def solution(food):
    answer = []
    result = ''
    num = 1
    
    for i in food[1:]:
        if i%2==1:
            i-=1
            answer.append(i//2)
        else:
            answer.append(i//2)
    
    for cnt in answer:
        result += cnt*str(num)
        num += 1
    
    result = (result + "0" + result[::-1])
    
    if len(result)>=3:
        return result