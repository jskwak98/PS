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


# 좀비 떼 잡기 문제
# O(n)으로 풀 수 있는 문제
# 핵심은 machine gun range안에 들어온 적이 벙커 바로 앞에 도달하기 전 받는 최종 데미지는
# 자신의 ml-1 칸 앞에 있는 좀비들이 얼마나 폭탄을 많이 사용하게 했는지에 달려있음
# 처음부터 ml 안이었던 적은,(떨어진 칸수 - c 사용횟수) * mk
# ml 밖은 mk * ml이 기본데미지고 c가 사용된 횟수만큼 mk 차감
# 결국 c 사용횟수를 count할 queue를 만들고 sum 대신
# append popleft단계의 값만 사용횟수에 업데이트한다면
# deque는 O(1)
# 데이터는 n 길이므로
# O(n) 시간 안에 돌아간다.

"""
6
3 2
1
2
4
6
6
6
8

YES

6
3 2
2
3
4
6
6
6
6

NO
"""