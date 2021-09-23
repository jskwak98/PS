from itertools import product


class NumParser:
    """
    make a parser that make all possible permutations of numbers
    and evaluate the equation
    """
    def __init__(self, n):
        self.num = [str(i) for i in range(2, n+1)]
        self.ops = product([" ", "+", "-"], repeat=n-1)

    def make(self):
        for op in self.ops:
            stc = "1" + "".join(map(lambda x: x[0]+x[1], zip(op, self.num)))
            p_stc = "".join(stc.split(" "))
            if eval(p_stc) == 0:
                print(stc)


def solution():
    case = int(input())
    for _ in range(case):
        np = NumParser(int(input()))
        np.make()
        print()


solution()

"""
input
2
3
7

output
1+2-3

1+2-3+4-5-6+7
1+2-3-4+5+6-7
1-2 3+4+5+6+7
1-2 3-4 5+6 7
1-2+3+4-5+6-7
1-2-3-4-5+6+7
"""