# https://school.programmers.co.kr/learn/courses/30/lessons/43238

from typing import List
from bisect import bisect_left
from collections import defaultdict
from itertools import combinations

def solution(info: List[str], query: List[str]) -> List[int]:
    answer = []
    people = defaultdict(list)
    
    for i in info:
        person = i.split()
        score = int(person.pop())
        people[''.join(person)].append(score)
        
        for j in range(4):
            case = list(combinations(person, j))
            for c in case:
                people[''.join(c)].append(score)
                
    for i in people:
        people[i].sort()
        
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        answer.append(len(people[key]) - bisect_left(people[key], score))
        
    return answer
