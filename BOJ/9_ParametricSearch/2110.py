import sys


def solution():
    input = sys.stdin.readline
    houses = []
    n, c = map(int, input().split())
    for _ in range(n):
        houses.append(int(input()))
    houses = sorted(houses)

    left = 1
    right = houses[-1] - houses[0]
    ans = houses[1] - houses[0]

    while left <= right:
        cur = houses[0]
        mid = (left + right) // 2
        count = 1

        for index in range(1, n):
            dist = houses[index] - cur
            if dist >= mid:
                cur = houses[index]
                count += 1

        if count >= c:
            # 탐색시, 현재 mid, 즉 공유기간 최소거리를 기준으로 설치했을 때
            # c보다 많이 공유기가 설치된 경우, 공유기간 설치 최소거리, mid를
            # 증가시켜줘야함, left를 높게 해준다.
            left = mid + 1
            ans = mid
        else:
            # 탐색시, 현재 mid, 즉 공유기간 최소거리를 기준으로 설치했을 때
            # c보다 적게 공유기가 설치된 경우, 공유기간 설치 최소거리를 줄여줘야한다
            # right를 mid-1로 이분탐색해준다.
            right = mid - 1

    print(ans)


if __name__ == "__main__":
    solution()