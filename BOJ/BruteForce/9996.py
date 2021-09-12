def check(head, tail, text):
    if len(head) + len(tail) > len(text):
        print('NE')
        return
    if text[:len(head)] == head and text[len(text)-len(tail):] == tail:
        print('DA')
        return
    else:
        print('NE')
        return


def solution():
    n = int(input())
    pattern = tuple(input().split('*'))
    for _ in range(n):
        text = input()
        check(pattern[0], pattern[1], text)


solution()