from collections import defaultdict


def solution():
    n, m, k = map(int, input().split())
    bests = defaultdict(float)
    for _ in range(m):
        data = input().split()
        for i in range(0, 2 * m, 2):
            participant, score = int(data[i]), float(data[i + 1])
            if bests[participant] < score:
                # for each participant, you only consider their best score
                bests[participant] = score
    print(round(sum(sorted(bests.values(), reverse=True)[:k]), 1))


solution()

"""
input
4 4 3
4 5.0 2 4.0 3 2.0 1 1.0
2 2.0 3 1.0 1 0.5 4 0.3
4 6.0 3 5.0 2 2.0 1 0.0
1 4.0 2 3.0 4 0.6 3 0.3

output
15.0
"""