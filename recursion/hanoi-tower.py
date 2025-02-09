# https://school.programmers.co.kr/learn/courses/30/lessons/12946

from typing import List

def hanoi(n: int, start: int, mid: int, to: int, answer: List[List[int]]) -> List[List[int]]:
    if n == 1:
        return answer.append([start, to])
    hanoi(n - 1, start, to, mid, answer)
    answer.append([start, to])
    hanoi(n - 1, mid, start, to, answer)
  

def solution(n: int) -> List[List[int]]:
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer
