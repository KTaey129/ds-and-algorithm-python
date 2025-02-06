# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def radixChange(num: int, radix: int) -> str:
    if num == 0:
        return '0'
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return ''.join(reversed(nums))

def solution(n: int) -> int:
    return int(radixChange(n, 3)[::-1], 3)
