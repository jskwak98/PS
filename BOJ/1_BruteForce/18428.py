from itertools import combinations
from copy import deepcopy


def check(teachers, obstacles):
    """
    You have students checked by teacher in teachers dictionary, key : teacher, value : students set
    by checking obstacles are in between students and teacher, you erase them from
    deep copied dictionary ts.
    at final, if you check there's no one left in ts, the obstacles have
    successfully hindered teachers' sights
    """
    ts = deepcopy(teachers)
    for obstacle in obstacles:
        for teacher in teachers:
            for student in teachers[teacher]:
                if teacher[0] == student[0] == obstacle[0] and min(teacher[1], student[1]) < obstacle[1] < max(teacher[1], student[1]):
                    if student in ts[teacher]:
                        ts[teacher].remove(student)
                elif teacher[1] == student[1] == obstacle[1] and min(teacher[0], student[0]) < obstacle[0] < max(teacher[0], student[0]):
                    if student in ts[teacher]:
                        ts[teacher].remove(student)
    for teacher in ts:
        if len(ts[teacher]) != 0:
            return False
    return True


def solution():
    """
    I've made candidates for obstacle positions, then went through all 3 combinations
    of those candidates. For speed and efficiency I've checked if there's case that
    teacher is adjacent to student. In such case it's trivial that obstacle cannot
    hinder teacher's sight.
    teachers is dictionary consisted of key : teacher and values : set of students being watched by the teacher
    """
    n = int(input())
    board = []
    teachers = dict()
    students = set()
    candidates = []
    for row in range(n):
        board.append(input().split())
        for col in range(n):
            if board[row][col] == 'T':
                teachers[(row, col)] = set()
            elif board[row][col] == 'S':
                students.add((row, col))
    for teacher in teachers:
        for student in students:
            if teacher[0] == student[0]:
                if abs(teacher[1] - student[1]) == 1:  # no space exists between S and T
                    print("NO")
                    return
                else:
                    teachers[teacher].add(student)
                    for col in range(min(teacher[1], student[1])+1, max(teacher[1], student[1])):
                        candidate = (teacher[0], col)
                        if candidate not in students and candidate not in teachers and candidate not in candidates:
                            candidates.append(candidate)
            elif teacher[1] == student[1]:
                if abs(teacher[0] - student[0]) == 1:  # no space exists between S and T
                    print("NO")
                    return
                else:
                    teachers[teacher].add(student)
                    for row in range(min(teacher[0], student[0])+1, max(teacher[0], student[0])):
                        candidate = (row, teacher[1])
                        if candidate not in students and candidate not in teachers and candidate not in candidates:
                            candidates.append(candidate)
    if len(candidates) <= 3:
        print("YES")
        return
    for obstacles in combinations(candidates, 3):
        if check(teachers, obstacles):
            print("YES")
            return
    print("NO")
    return


solution()

"""
example

input
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

output
YES

input
4
S S S T
X X X X
X X X X
T T T X

output
NO
"""