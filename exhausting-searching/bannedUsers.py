# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from typing import List
import re

def search(idx, visit, userId, answer, banPatterns):
    if idx == len(banPatterns):
        answer.add(visit)
        return
    for i in range(len(userId)):
        if (visit & (1 << i)) > 0 or not re.fullmatch(banPatterns[idx], userId[i]):
            continue
        search(idx + 1, visit | (1 << i), userId, answer, banPatterns)

def solution(userId: List[str], bannedId: List[str]) -> int:
    answer = set()
    banPatterns = [x.replace('*', '.') for x in bannedId]
    search(0, 0, userId, answer, banPatterns)
    
    return len(answer)

