#https://school.programmers.co.kr/learn/courses/30/lessons/76503

answer = 0
import sys
sys.setrecursionlimit(300000)

def dfssum(me, parent, a, mat):
    global answer
    for node in mat[me]:
        if node != parent:
            t = dfssum(node, me, a, mat)
            a[me] += t
            answer += abs(t)
    if parent != None:
        temp = a[me]
        a[me] = 0
        return temp
    else:
        return a[me]

def solution(a, edges):
    global answer
    if sum(a) != 0:
        return -1
    mat = [set() for _ in range(len(a))]
    for e in edges:
        mat[e[0]].add(e[1])
        mat[e[1]].add(e[0])
    first = dfssum(0, None, a, mat)
    if first == 0:
        return answer
    else:
        return -1
    
"""
[-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]
9

[0, 1, 0], [[0, 1], [1, 2]]
-1
"""