# https://school.programmers.co.kr/learn/courses/30/lessons/87377?language=python3

from typing import List

def solution(line: List[List[int]]) -> List[str]:
    answer, intersection = [], []
    x_max = -1e15
    x_min = 1e15
    y_max = -1e15
    y_min = 1e15

    # get intersections
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            
            denominator = a * d - b * c
            if denominator == 0: continue
            
            x = (b * f - e * d) / denominator
            y = (e * c - a * f) / denominator
            
            if x == int(x) and y == int(y):
                x, y = int(x), int(y)
                intersection.append((x, y))

    # exception
    if not intersection: return []

    # get size of rectangle
    for x, y in intersection:
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
                
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [['.'] * x_len for row in range(y_len)]

    # draw stars
    for star_x, star_y in intersection:
        nx = star_x - x_min
        ny = star_y - y_min
        coord[ny][nx] = '*'
        
    return [''.join(row) for row in coord[::-1]]
        
    
    
