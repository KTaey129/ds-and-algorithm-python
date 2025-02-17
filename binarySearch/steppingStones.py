# https://school.programmers.co.kr/learn/courses/30/lessons/43236

from typing import List

def solution(distance: int, rocks: List[int], n: int) -> int:
    answer = 0
    start, end = 0, distance
    rocks.append(distance)
    rocks.sort()
    
    while start <= end:
        mid = (start + end) // 2
        removed = 0
        prev = 0
        
        for rock in rocks:
            if rock - prev < mid: 
                removed +=1
            else:
                prev = rock
                
            if removed > n:
                break
            
        if removed > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
            
    return answer
                
            
