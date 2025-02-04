# https://school.programmers.co.kr/learn/courses/30/lessons/68645

from typing import List

def solution(n: int) -> List[int]:
  
    # generate n * n matrix
    # fill the matrix counterclockwise, spiral shape
    # change direction at the ends
    # return when you fill the triangle fully
    
    snail = [[0] * i for i in range(1, n + 1)]
    
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    x = y = angle = 0
    cnt = 1
    size = n * (n + 1) // 2
    while cnt <= size:
        snail[y][x] = cnt
        ny = y + dy[angle]
        nx = x + dx[angle]
        cnt += 1
        
        if 0 <= ny < n and 0 <= nx <= ny and snail[ny][nx] == 0:
            y, x = ny, nx
        else:
            angle = (angle + 1) % 3
            y += dy[angle]
            x += dx[angle]
        
    
    return [i for j in snail for i in j]
