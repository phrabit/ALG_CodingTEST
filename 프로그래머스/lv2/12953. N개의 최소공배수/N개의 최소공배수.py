# 나의 풀이
# -> 가장 큰수와 가장 작은수의 최소공배수를 구하고, 가장 작은 수 pop
# -> 이 과정을 arr 원소가 하나 남을 때(모든 수의 최소공배수)까지 하기.
def solution(arr):
    lcm = 0
    
    while True:
        
        if len(arr)==1:
            break;
        
        #1. arr 내림차순 정렬 - 편의를 위해
        arr = sorted(arr, reverse=True)
    
        #2. 최대값 최소값의 최소공배수 반복적으로 구함.
        min = arr[-1]
        max = arr[0]
        tmp = 0
        tmp_li = []

        for i in range(2, min+1):        
            if min%i==0 and max%i==0:
                tmp_li.append(i)

        glm=1 if len(tmp_li) == 0 else tmp_li[-1]

        tmp = glm * (max//glm) * (min//glm)
        arr[0] = tmp
        arr.pop()
    
    return arr[0]
    
                