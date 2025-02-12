# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from typing import List, Set
import re
from itertools import permutations

def search(idx: int, visit: int, userId: List[str], answer: Set[int], banPatterns: List[str]) -> None:
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



def solution2(userId: List[str], bannedId: List[str]) -> int:
    answer = set()
    banned = ' '.join(bannedId).replace('*', '.')
    for i in permutations(userId, len(bannedId)):
        if re.fullmatch(banned, ' '.join(i)):
            answer.add(''.join(sorted(i)))
            
    return len(answer)
