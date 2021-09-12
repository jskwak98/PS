from itertools import combinations


def three_max(cards):
    return max(map(lambda x: sum(x) % 10, combinations(cards, 3)))


def solution():
    n = int(input())
    ans = None
    max_sum = -1
    for i in range(1, n+1):
        cards = list(map(int, input().split()))
        if three_max(cards) >= max_sum:
            ans = i
    print(i)

solution()