def check(head, tail, text):
    """
    checks if head of the text matches with pattern
    and tail of the text matches with pattern
    """
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

"""
input
3
a*d
abcd
anestonestod
facebook

output
DA
DA
NE

input
6
h*n
huhovdjestvarnomozedocisvastan
honijezakon
atila
je
bio
hun

output
DA
DA
NE
NE
NE
DA
"""