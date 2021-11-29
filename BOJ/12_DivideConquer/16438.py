import sys
from collections import deque
from math import log2, ceil


def divide(n):
    left_n = n//2
    right_n = n - left_n
    return 'A' * left_n + 'B' * right_n, left_n, right_n


def solution():
    input = sys.stdin.readline
    n = int(input())
    q = deque([n])
    trials_to_consider = ceil(log2(n))
    for _ in range(trials_to_consider):
        monkey_composition = []
        division_n = len(q)
        for _ in range(division_n):
            substr, rn, ln = divide(q.popleft())
            monkey_composition.append(substr)
            q.append(rn)
            q.append(ln)
        print("".join(monkey_composition))
    for _ in range(7 - trials_to_consider):
        print('B'*1 + 'A'*(n-1))


if __name__ == "__main__":
    solution()

"""
divide and conquer
그리디하게 생각할 수 있다.
첫 날 둘로 한번 나누고 나면 양 그룹은 한 번 적으로 대진한 것이기에,
다음 날에는 각 그룹별로 고려하면 된다.
128마리 원숭이까지 7일 내로 해결 가능
7을 예시로 하면 다음과 같다.

AAAA  BBB

AA BB AA B

A B A B A B A
"""
