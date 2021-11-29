import sys


def conquer(fold):
    mid = len(fold) // 2
    for i in range(mid):
        if fold[i] == fold[mid * 2 - i]:
            return False
    return True


def divide_check(fold):
    if len(fold) == 1:
        return True
    mid = len(fold) // 2
    if conquer(fold):
        return divide_check(fold[:mid]) and divide_check(fold[mid+1:])
    else:
        return False


def solution():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        print("YES" if divide_check(input().strip()) else "NO")


if __name__ == "__main__":
    solution()