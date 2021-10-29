import sys


class Task:
    def __init__(self, score, duration):
        self.score = score
        self.duration = duration

    def do_work(self):
        self.duration -= 1
        return self.duration == 0

    def get_score(self):
        return self.score


def solution():
    n = int(input())
    stack = []
    ans = 0
    for query in sys.stdin.readlines():
        query = tuple(map(int, query.split()))
        if query[0]:
            new_task = Task(query[1], query[2])
            stack.append(new_task)
            job_finished = stack[-1].do_work()
            if job_finished:
                ans += stack[-1].get_score()
                stack.pop()
        else:
            if stack:
                job_finished = stack[-1].do_work()
                if job_finished:
                    ans += stack[-1].get_score()
                    stack.pop()
    print(ans)


if __name__ == "__main__":
    solution()

# input = sys.stdin.readline
# 으로 바꿔서 하는 버릇을 들이자.