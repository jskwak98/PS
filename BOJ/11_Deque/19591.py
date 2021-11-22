import sys
import re
from collections import deque


class Calculator:
    def __init__(self, num_str):
        split_nums = re.split(r"[\-\*\/\+]", num_str)
        if split_nums[0] == '':
            del split_nums[0]
        split_op = re.split(r"[0-9]+", num_str)
        self.calc = deque()
        for i in range(len(split_nums)):
            if i == 0:
                self.calc.append(int(split_op[i] + split_nums[i]))
            else:
                self.calc.append(split_op[i])
                self.calc.append(int(split_nums[i]))

    def calculate(self):
        while len(self.calc) > 1:
            front, end = (self.calc[0], self.calc[1], self.calc[2]), (self.calc[-3], self.calc[-2], self.calc[-1])
            if self.is_front_first(front, end):
                num1 = self.calc.popleft()
                op = self.calc.popleft()
                num2 = self.calc.popleft()
                self.calc.appendleft(self.evaluate(num1, op, num2))
            else:
                num2 = self.calc.pop()
                op = self.calc.pop()
                num1 = self.calc.pop()
                self.calc.append(self.evaluate(num1, op, num2))
        print(self.calc[0])

    def is_front_first(self, front, end):
        fe_num = self.front_or_end(front[1], end[1])
        if fe_num == 1:
            return True
        elif fe_num == -1:
            return False
        else:
            return self.evaluate(front[0], front[1], front[2]) >= self.evaluate(end[0], end[1], end[2])

    def front_or_end(self, front_op, end_op):
        first_ops = {'/', '*'}
        front = 1 if front_op in first_ops else 0
        end = 1 if end_op in first_ops else 0
        if front > end:
            return 1
        elif front == end:
            return 0
        else:
            return -1

    def evaluate(self, num1, op, num2):
        if op == '/':
            return self.div(num1, num2)
        elif op == '*':
            return num1 * num2
        elif op == '+':
            return num1 + num2
        else:
            return num1 - num2

    def div(self, a, b):
        return int(a/b)


def solution():
    input = sys.stdin.readline
    weird = Calculator(input())
    weird.calculate()


if __name__ == "__main__":
    solution()


"""
양심에 찔리지만 pypy3 썼음
규칙에 따라 구현하는 문제임
eval 쓰면 시간 오래 걸릴다는 사실을 알았다.
"""