#<나의 코드> - 맞음

def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        li = sorted(array[i-1:j])
        answer.append(li[k-1])
    
    return answer


# <답안 코드> - 더 깔끔함.

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer