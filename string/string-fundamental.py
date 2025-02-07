# https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s: str) -> bool:
    return len(s) in {4, 6} and s.isdigit()

import re

def solution(s: str) -> bool:
    return len(s) in {4, 6} and bool(re.match('^[0-9]*$', s))
