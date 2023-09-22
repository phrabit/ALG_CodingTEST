# def solution(n, words):
#     answer = [0, 0]

#     for i in range(1, len(words)):
#         if words[i-1][-1] != words[i][0]: # 1) 앞 사람 단어의 마지막 글자로 시작하지 않을 때
#             answer = [(i%n)+1 , (i//n)+1]
#             break;
#         elif words[i-1] in words[i:]: # 2) 말한 단어를 똑같이 말할 때
#             for idx in range(i, len(words[i:]) + 1):
#                 if words[i-1] == words[idx]:
#                     answer = [(idx%n)+1 , (idx//n)+1]
#                     break;

#     return answer

def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]: # 1) 앞 사람 단어의 마지막 글자로 시작하지 않을 때
            answer = [(i%n)+1 , (i//n)+1]
            break;
        elif words[i] in words[:i]: # 2) 말한 단어를 똑같이 말할 때
            answer = [(i%n)+1 , (i//n)+1]
            break;
        else:
            answer = [0,0]

    return answer


# 다른 사람의 풀이
# def solution(n, words):
#     for i in range(1, len(words)):
#         if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
#             return [(i%n)+1, (i//n)+1]
#     else:
#         return [0,0]
