import sys


def solution():
    input = sys.stdin.readline
    n = int(input())
    order = list(map(int, input().split()))
    r_order = list(reversed(order))
    want = list(map(int, input().split()))
    from_dex = order.index(want[0])
    from_r_dex = n - from_dex - 1
    to_check = order[from_dex:n] + order[0:from_dex]
    if to_check == want:
        print("good puzzle")
        return
    else:
        to_check = r_order[from_r_dex:n] + r_order[0:from_r_dex]
        if to_check == want:
            print("good puzzle")
            return
        else:
            print("bad puzzle")
            return


if __name__ == "__main__":
    solution()


"""
이렇게 해도 O(N)이긴 해서 풀린다.


5
1 2 3 4 5
4 3 2 1 5

good puzzle



5
1 2 3 4 5
1 2 4 3 5

bad puzzle
"""