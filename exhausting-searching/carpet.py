# https://school.programmers.co.kr/learn/courses/30/lessons/42842

from typing import List

def solution(brown: int, yellow: int) -> List[int]:
    grid = brown + yellow
    for n in range(3, int(grid ** 0.5) + 1):
        if grid % n != 0:
            continue
        m = grid // n
        if (n - 2) * (m - 2) == yellow:
            return [m, n]
