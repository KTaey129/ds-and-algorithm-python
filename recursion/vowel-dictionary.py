# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from typing import List

def find(data: List[str], p: str, step: int) -> None:
    if step == 6: return
    if p != '':
        data.append(p)
    for c in ['A', 'E', 'I', 'O', 'U']:
        find(data, p + c, step + 1)
    
def solution(word: str) -> int:
    answer = 0
    data = []
    find(data, '', 0)
    # return data.index(word) + 1
    for i in range(len(data)):      
        if data[i] == word:
            answer = i + 1
            break
                
    return answer

