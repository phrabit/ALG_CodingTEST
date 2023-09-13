def solution(s):
    
    answer = ""
    
    li = sorted(list(map(int, s.split(" "))))
    answer += (str(li[0]) + " " + str(li[-1]))
    
    return answer