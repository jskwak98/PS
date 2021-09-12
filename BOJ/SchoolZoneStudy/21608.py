from collections import Counter


def near(rctuple, N):
    r = rctuple[0]
    c = rctuple[1]
    nears = []
    # top
    if r > 0:
        nears.append((r - 1, c))
    # bottom
    if r < N - 1:
        nears.append((r + 1, c))
    # right
    if c < N - 1:
        nears.append((r, c + 1))
    # left
    if c > 0:
        nears.append((r, c - 1))
    return nears


def most_like(mat, student_dic, student_sit_dic, student, N, seats):
    likes = student_dic[student]
    where_likes_sat = []
    candidates = []
    for like in likes:
        where_likes_sat.append(student_sit_dic[like])
    for seat in where_likes_sat:
        candidates.extend(near(seat, N))
    c = Counter(candidates)
    c = c.most_common()


student_dic = {}
student_sit_dic = {}

N = int(input())
for _ in range(N * N):
    data = list(map(int, input().split()))
    student_dic[data[0]] = data[1:]

mat = [[0] * N for _ in range(N)]

seats = []
for r in range(N):
    for c in range(N):
        seats.append((r, c))
