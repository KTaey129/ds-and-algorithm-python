# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    st = new_id.lower()  # Step 1: Convert to lowercase
    
    st = re.sub('[^a-z0-9\-_.]', '', st)  # Step 2: Remove invalid characters
    # [^...] → Negated character class: Matches anything not inside the brackets.
    # a-z → Matches lowercase letters.
    # 0-9 → Matches digits.
    # \-_. → Matches the characters -, _, and ..
    # Note: The - must be escaped (\) because it's a special character in regex (indicating a range like a-z).
    
    st = re.sub('\.+', '.', st)  # Step 3: Replace multiple dots with a single dot
    # \. → Matches a literal dot (.).
    # Note: We use \ to escape the dot because . is a special regex character (it means "any character").
    # + → Matches one or more occurrences of the previous character (.).
    
    st = re.sub('^[.]|[.]$', '', st)  # Step 4: Remove leading/trailing dots
    # ^. → Matches a dot (.) at the beginning of the string (^ means "start of string").
    # | → OR operator (matches either the left or right pattern).
    # .$ → Matches a dot (.) at the end of the string ($ means "end of string").
    
    if not st:  # Step 5: If empty, replace with "a"
        st = 'a'

    st = st[:15].rstrip('.')  # Step 6: Trim to 15 characters and remove trailing dot

    while len(st) < 3:  # Step 7: Extend if less than 3 characters
        st += st[-1]

    return st


def solution(new_id: str) -> str:
    answer = new_id.lower()
    filtered = []
    for s in answer:
        if s.isalpha() or s.isdigit() or s in ('-', '_', '.'):
            filtered.append(s)
    answer = ''.join(filtered)
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer = answer.strip('.')
    if answer == '':
        answer = 'a'
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) < 3:
        while len(answer) < 3:
            answer = answer + answer[-1]
            
    return answer
