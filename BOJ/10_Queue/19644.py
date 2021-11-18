import sys
from collections import deque


class CDeque:
    def __init__(self):
        self.queue = deque()
        self.c_in = 0

    def append(self, c_bool):
        # append whether you have to use c or not
        self.queue.append(c_bool)
        self.c_in += c_bool

    def popleft(self):
        self.c_in -= self.queue.popleft()

    def get_c_in(self):
        return self.c_in


def solution():
    input = sys.stdin.readline
    l = int(input())
    ml, mk = map(int, input().split())
    c = int(input())
    alive = True
    # 한번만 검사해도 될 것 같음, range 안에 있는 c 사용 좀비 수를 카운트 하며, mk * ml의 체력보다 많은지 뒤의 좀비들을 검사하자
    c_deque = CDeque()
    for i in range(l):
        zombie = int(input())
        if i < ml:
            if zombie <= mk * (i - c_deque.get_c_in() + 1):
                c_deque.append(0)
            else:
                c -= 1
                c_deque.append(1)
        else:
            if zombie <= mk * (ml - c_deque.get_c_in()):
                c_deque.append(0)
                c_deque.popleft()
            else:
                c -= 1
                c_deque.append(1)
                c_deque.popleft()
        if c < 0:
            alive = False
            break
    print("YES" if alive else "NO")


if __name__ == "__main__":
    solution()