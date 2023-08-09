# def solution(s):
#     answer = ""
#     for i in s.split():
#         if i[0].isalpha():
#             answer += (i[0].upper() + i[1:].lower() + " ")
#         else:
#             answer += (i.lower() + " ")
#     return answer.rstrip()

def solution(s):
    answer = []
    s = s.split(" ")
    for word in s:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append(word)
    return " ".join(answer)