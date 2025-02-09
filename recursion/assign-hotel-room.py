# https://school.programmers.co.kr/learn/courses/30/lessons/64063

from typing import List 
import sys

sys.setrecursionlimit(2000)

def find_emptyroom(chk: int, rooms: List[int]) -> List[int]:
    if chk not in rooms:
        rooms[chk] = chk + 1
        return chk
    empty = find_emptyroom(rooms[chk], rooms)
    rooms[chk] = empty + 1
    return empty

def solution(k: int, room_number: List[int]) -> List[int]:
    rooms = dict()
    for num in room_number:
        chk_in = find_emptyroom(num, rooms)
    return list(rooms)


def solution(k, room_number):
    room_dic = {}
    ret = []
    for i in room_number:
        n = i
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit: room_dic[j] = n + 1
    return ret
