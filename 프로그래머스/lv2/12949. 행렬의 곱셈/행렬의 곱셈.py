import numpy as np

def solution(arr1, arr2):
    result = np.dot(arr1, arr2)
    
    # ndarray 형태를 파이썬 list형태로 바꿔주기
    result = result.tolist()
    
    # print(answer)
    return result
    
    