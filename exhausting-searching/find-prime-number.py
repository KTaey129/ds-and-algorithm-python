# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def check_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers: str) -> int:
    unique_numbers = set()
    
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            num = int(''.join(perm))
            unique_numbers.add(num)
            
    return sum(1 for num in unique_numbers if check_prime(num))

