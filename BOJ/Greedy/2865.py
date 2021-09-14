from collections import defaultdict


def solution():
    n, m, k = map(int, input().split())
    bests = defaultdict(float)
    for _ in range(m):
        data = input().split()
        for i in range(0, 2 * m, 2):
            participant, score = int(data[i]), float(data[i + 1])
            if bests[participant] < score:
                bests[participant] = score
    print(round(sum(sorted(bests.values(), reverse=True)[:k]), 1))


solution()