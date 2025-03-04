# https://school.programmers.co.kr/learn/courses/30/lessons/42840

from typing import List

def solution(answers: List[int]) -> List[int]:
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []
    
    for idx, answer in enumerate(answers):
        if answer == student1[idx % len(student1)]:
            score[0] += 1
        if answer == student2[idx % len(student2)]:
            score[1] += 1
        if answer == student3[idx % len(student3)]:
            score[2] += 1
            
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)
            
    return result
