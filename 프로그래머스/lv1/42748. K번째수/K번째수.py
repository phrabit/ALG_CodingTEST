def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        li = sorted(array[i-1:j])
        answer.append(li[k-1])
    
    return answer
