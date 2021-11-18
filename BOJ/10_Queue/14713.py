import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    n = int(input())
    deque_list = []
    dic = {}
    for queue_num in range(n):
        deque_list.append(deque(input().split()))
        dic[deque_list[queue_num][0]] = queue_num
    for word in input().split():
        if word in dic:
            deque_list[dic[word]].popleft()
            if deque_list[dic[word]]:
                dic[deque_list[dic[word]][0]] = dic[word]
                dic.pop(word)
        else:
            print("Impossible")
            return
    for queue in deque_list:
        if len(queue) > 0:
            print("Impossible")
            return
    print("Possible")


if __name__ == "__main__":
    solution()

# deque를 1~100개 사이로 만들고
# 주어진 시퀀스가 deque의 첫 단어인지
# dictionary를 보며 정하면 된다
# 주어진 시퀀스가 모든 단어를 순서대로 뽑아내며 구성한 문장인지
# 확인하는 문제
# 메모리 효율을 위해 dictionary를 모든 단어에 대해 구성하지 않고
# 빼주고 넣어주고 한다 어차피 모두 unique한 단어라
# 다 넣어도 되긴 할거다
# 특이하게 edge case로 주어진 시퀀스가
# 모든 단어를 사용하지 않은 경우가 있다
# 마지막 for는 그걸 위해서다.

"""
3
i want to see you
next week
good luck
i want next good luck week to see you

Possible

2
i found
an interesting cave
i found an cave interesting

Impossible
"""