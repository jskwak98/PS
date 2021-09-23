from heapq import *


def solution():
    """
    put all assignments in heap,
    make an max heap with respect to the score
    pop(get the highest score assignment) and check
    if it can fit into current schedule
    """
    n = int(input())
    reserved = [0] * 1000
    h = []
    total = 0
    for _ in range(n):
        d, w = map(int, input().split())
        heappush(h, (-w, d))
    while h:
        w, d = heappop(h)
        if sum(reserved[:d]) != d:
            for i in range(d-1, -1, -1):
                if reserved[i] == 0:
                    reserved[i] = 1
                    total -= w
                    break
    print(total)


solution()

"""
input
7
4 60
4 40
1 20
2 50
3 30
4 10
6 5

output
185
"""