# <나의 코드> -> 틀림
# 왜냐면, 앞자리수만 정렬되었으므로, 앞자리가 같은 경우 정렬이 제대로 되지 않음
# 3 30 34 순으로 되어있음... 정답은 34 3 30

# def solution(numbers):
    
#     numbers = list(map(str, numbers))
#     li = sorted(numbers, key = lambda x: -int(x[0]))
#     result = ("".join(li))
#     return result





#################################################################
# <답안 코드>
def solution(numbers):
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # 2. lambda x : x * 3은 num 인자 각각의 문자열을 3번 반복한다는 뜻이다. Q. x * 3을 하는 이유? -> num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    # Q. int로 변환한 뒤, 또 str로 변환해주는 이유?
    # 모든 값이 0일 때(즉, ‘000’을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다.
    answer = str(int(''.join(numbers)))
    
    return answer