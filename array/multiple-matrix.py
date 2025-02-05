# https://school.programmers.co.kr/learn/courses/30/lessons/12949
# you can use numpy module otherwise

from typing import List

def solution(arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
    
    # generate initial result matrix
    # conduct multiplication
    
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]
                
    return result
