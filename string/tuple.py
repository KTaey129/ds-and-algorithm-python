# https://school.programmers.co.kr/learn/courses/30/lessons/64065

from typing import List

def solution(s: str) -> List[int]:
    data = s[2:-2].split('},{')
    data = sorted(data, key=lambda x: len(x))
    answer = []
    for item in data:
        item = list(map(int, item.split(',')))
        for value in item:
            if value not in answer:
                answer.append(value)
                
    return answer



def solution2(s: str) -> List[int]:
    answer = {}
    s = sorted(s[2:-2].split('},{'), key=len)
    for tuples in s:
        elements = tuples.split(',')
        for element in elements:
            number = int(element)
            if number not in answer:
                answer[number] = 1
                
    return list(answer)
