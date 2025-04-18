# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import re
from typing import List, Dict

def toPostFix(tokens: List[str], priority: Dict[int, List[str]]) -> str:
    stack = []
    postfix = []
    
    for token in tokens:
        if token.isdigit(): 
            postfix.append(token)
        else:
            if not stack:
                stack.append(token)
            else:
                while stack:
                    if priority[token] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    else:
                        break
                    
                stack.append(token)
                
    while stack:
        postfix.append(stack.pop())
        
    return postfix

def calc(tokens: str) -> int:
    stack = []
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue
            
        num1 = stack.pop()
        num2 = stack.pop()
        
        if token == '*':
            stack.append(num2 * num1)
        elif token == '+':
            stack.append(num2 + num1)
        else:
            stack.append(num2 - num1)
            
    return stack.pop()

def solution(expression: str):
    tokens = re.split(r'([-+*])|\s+', expression)
    # tokens = re.split(r'([-+*])', expression)
    operators = ['+', '-', '*']
    answer = 0
    
    for i in map(list, permutations(operators)):
        priority = {o:p for p, o in enumerate(list(i))}
        postfix = toPostFix(tokens, priority)
        answer = max(answer, abs(calc(postfix)))
        
    return answer
        
