# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def facto(i: int) -> int:
    if i < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if i < 2 else i * facto(i - 1)

def collatz(num: int, answer: int) -> int:
    if num == 1:
        return answer
    if answer == 500:
        return -1
    if num % 2 == 0:
        return collatz(num // 2, answer + 1)
    elif num % 2 == 1:
        return collatz(num * 3 + 1, answer + 1)

def solution(num: int) -> int:
    return collatz(num, 0)
