# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s: str) -> str:
    s = list(s)
    num = 0
    for i in range(len(s)):
        if s[i] == ' ':
            num = 0
            continue
        else:
            s[i] = s[i].upper() if num % 2 == 0 else s[i].lower()
            num += 1
                       
               
    return ''.join(s)
