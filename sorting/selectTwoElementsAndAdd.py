from typing import List
from itertools import combinations

def solution(numbers: List[int]) -> List[int]:
    selects = list(combinations(numbers, 2))
    answer = set()
    for select in selects:
        (a, b) = select
        answer.add(a + b)
        
    return sorted(answer)


def solution2(numbers: List[int]) -> List[int]:
    select = {numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i + 1, len(numbers))}
    return sorted(select)
