def solution(phone_number: str) -> str:
    len_s = len(phone_number)
    new_number = ['*' for i in range(len_s - 4)]
    new_s = ''.join(new_number) + phone_number[-4:]
    
    return new_s

def solution(phone_number: str) -> str:
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

