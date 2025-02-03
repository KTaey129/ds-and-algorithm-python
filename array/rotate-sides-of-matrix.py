# https://school.programmers.co.kr/learn/courses/30/lessons/77485

from typing import List

# function to rotate clockwise
def rotate(x1: int, y1: int, x2: int, y2: int, matrix: List[List[int]]) -> int:
    first = matrix[x1 - 1][y1 - 1]
    min_value = first
    
    # left
    for i in range(x1 - 1, x2 - 1):
        matrix[i][y1 - 1] = matrix[i + 1][y1 - 1]
        min_value = min(min_value, matrix[i][y1 - 1])
        
    # bottom
    for i in range(y1 - 1, y2 - 1):
        matrix[x2 - 1][i] = matrix[x2 - 1][i + 1]
        min_value = min(min_value, matrix[x2 - 1][i])
        
    # right
    for i in range(x2 - 1, x1 - 1, -1):
        matrix[i][y2 - 1] = matrix[i - 1][y2 - 1]
        min_value = min(min_value, matrix[i][y2 - 1])
        
    # top
    for i in range(y2 - 1, y1, -1):
        matrix[x1 - 1][i] = matrix[x1 - 1][i - 1]
        min_value = min(min_value, matrix[x1 - 1][i])
        
    matrix[x1 - 1][y1] = first
        
    return min_value

def solution(rows: int, columns: int, queries: List[List[int]]) -> List[int]:
    answer = []  
    
    # generate initial matrix    
    init = [[i * columns + (j + 1) for j in range(columns)] for i in range(rows)]
            
    # get coordinates to rotate for each query. rotate and get result
    for x1, y1, x2, y2 in queries:
        
        answer.append(rotate(x1, y1, x2, y2, init))
    
    
    return answer
