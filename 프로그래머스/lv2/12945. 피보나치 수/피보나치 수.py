#재귀호출 사용시, 시간초과 발생!!
#리스트로 만들어서, 해결해야함.

def solution(n):
    answer = []
    for i in range(n+1):
        if i==0 or i==1:
            answer.append(i)
        else:
            f = answer[i-1] + answer[i-2]
            answer.append(f % 1234567)

    return answer[-1]
    
