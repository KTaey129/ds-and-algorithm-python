# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s: str) -> int:
    answer = len(s)
    for x in range(1, len(s) // 2 + 1):
        comp_len = 0
        comp = ''
        cnt = 1
        for i in range(0, len(s) + 1, x):
            temp = s[i:i + x]
            if comp == temp:
                cnt += 1
            elif comp != temp:
                comp_len += len(temp)
                if cnt > 1:
                    comp_len += len(str(cnt))
                cnt = 1
                comp = temp
        
        answer = min(answer, comp_len)
    
    return answer
