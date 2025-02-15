# https://school.programmers.co.kr/learn/courses/30/lessons/42746

from typing import List

def solution(numbers: List[int]) -> str:
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x * 3, reverse=True)
    result = ''.join(numbers)
    if '0' * len(numbers) == result: return '0'
    return result
