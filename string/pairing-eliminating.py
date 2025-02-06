# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s: str) -> int:  
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    return 1 if not stack else 0
