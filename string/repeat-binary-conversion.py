# https://school.programmers.co.kr/learn/courses/30/lessons/64065

from typing import List

def solution(s: str) -> List[int]:
    change, zero = 0, 0
    while s != '1':
        change += 1
        num = s.count('1')
        zero += len(s) - num
        s = bin(num)[2:]
        
    return [change, zero]


# bin(num): Converts num (an integer) to a binary string, prefixed with "0b".
# Example: bin(5) → "0b101"
# [2:]: Removes the "0b" prefix to get only the binary digits.
# Example: "0b101"[2:] → "101"
