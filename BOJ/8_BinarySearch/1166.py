def solution():
    n, l, w, h = tuple(map(int, input().split()))
    right = max(l, w, h)
    left = 0
    #epsilon = 1e-9
    #while abs(right-left) >= epsilon:
    for _ in range(100000):
        mid = (right + left) / 2
        if (l // mid) * (w // mid) * (h // mid) < n:
            right = mid
        else:
            left = mid
    print(mid)

if __name__ == "__main__":
    solution()


"""
77 146 523 229

52.300000000000004
"""