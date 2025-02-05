# base change code (from 10 to radix)
def radixChange(num: int, radix: int) -> str:
    if num == 0: return '0'

    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return ''.join(reversed(nums))


def solution(s: str, n: int) -> str:
    answer = []
    for i in s:
        if 'a' <= i <= 'z':
            answer.append(chr(ord('a') + ((ord(i) - ord('a') + n) % 26)))
        elif 'A' <= i <= 'Z':
            answer.append(chr(ord('A') + ((ord(i) - ord('A') + n) % 26)))
        else:
            answer.append(i)
    
    
    return ''.join(answer)
