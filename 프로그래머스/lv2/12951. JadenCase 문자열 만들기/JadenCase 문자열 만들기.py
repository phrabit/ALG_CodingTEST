# 나의 풀이 테스트케이스 8 실패

# def solution(s):
#     answer = ''
    
#     words = s.split(" ")
#     for word in words:
#         answer += (word.capitalize()+" ")
    
#     return answer.rstrip()


def solution(s):
    answer = []
    
    words = s.split(" ")
    for word in words:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append(word)
    
    return " ".join(answer)