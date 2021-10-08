class Dice:
    """
    dice class which you can roll to right left down
    """
    def __init__(self):
        self.top = 1
        self.east = 3
        self.west = 4
        self.north = 5
        self.south = 2
        self.bottom = 6

    def right_roll(self):
        self.top, self.east, self.bottom, self.west = self.west, self.top, self.east, self.bottom

    def left_roll(self):
        self.top, self.east, self.bottom, self.west = self.east, self.bottom, self.west, self.top

    def down_roll(self):
        self.top, self.south, self.bottom, self.north = self.north, self.top, self.south, self.bottom

    def round_sum(self):
        return self.top + self.east + self.bottom + self.west


def solution():
    r, c = map(int, input().split())
    quotient, remainder = divmod(c-1, 4)
    ans = 0
    dice = Dice()
    for row in range(r):
        ans += dice.top
        if row % 2 == 0:
            if quotient > 0:
                ans += dice.round_sum() * quotient
            for _ in range(remainder):
                dice.right_roll()
                ans += dice.top
        else:
            if quotient > 0:
                ans += dice.round_sum() * quotient
            for _ in range(remainder):
                dice.left_roll()
                ans += dice.top
        dice.down_roll()
    print(ans)


solution()


"""
3 2
19

3 4
42

737 296
763532
"""