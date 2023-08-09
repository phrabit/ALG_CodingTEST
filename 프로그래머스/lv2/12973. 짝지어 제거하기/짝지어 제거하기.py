def solution(s):
    stack = []
    for i in s:
        if len(stack)==0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    return 1 if len(stack) == 0 else 0