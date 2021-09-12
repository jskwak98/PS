from collections import deque
from collections import Counter


def rotate(belt, robot):
    belt.appendleft(belt.pop())
    robot.pop()
    robot.appendleft(0)
    if robot[-1]:
        robot[-1] = 0


def robot_walk(belt, robot):
    for r_dex in range(len(robot)-2, -1, -1):
        if robot[r_dex] and not robot[r_dex+1] and belt[r_dex+1] >= 1:
            robot[r_dex] = 0
            robot[r_dex+1] = 1
            if r_dex+1 == len(robot) - 1:
                robot[r_dex + 1] = 0
            belt[r_dex+1] -= 1


def robot_on_belt(belt, robot):
    if belt[0] != 0:
        belt[0] -= 1
        robot[0] = 1


def durability_test(belt, K):
    counter = Counter(belt)
    if counter[0] >= K:
        return False
    return True



N, K = list(map(int, input().split()))
belt = deque(map(int, input().split()))
robot = deque([0]*N)

t = 0
flag = True
while flag:
    t += 1
    rotate(belt, robot)
    robot_walk(belt, robot)
    robot_on_belt(belt, robot)
    flag = durability_test(belt, K)

print(t)
