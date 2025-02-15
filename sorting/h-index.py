# https://school.programmers.co.kr/learn/courses/30/lessons/42747

from typing import List

def solution(citations: List[int]) -> int:
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    
    return 0
