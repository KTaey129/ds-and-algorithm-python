# https://school.programmers.co.kr/learn/courses/30/lessons/12915

from typing import List

def solution(strings: List[str], n: int) -> List[str]:
    return sorted(sorted(stirngs), key=lambda x: x[1])
