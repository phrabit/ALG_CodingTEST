# 나의 코드 - 맞음

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
    
##############################################################################
    
    
# <답안 코드> - 깔끔함

def solution(food): # 준비한 음식은 항상 짝수개 , 갯수가 1개라면, 패스한다. 홀수개라면 //2 
    food_str = ""
    for i in range(len(food)):
        cnt = food[i] // 2
        food_str += str(i)*cnt
    food_str = food_str+"0"

    return food_str+ food_str[0:-1][::-1]
