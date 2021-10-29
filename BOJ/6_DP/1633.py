import heapq as hq
import sys


class ChessTeam:
    def __init__(self):
        self.blacks = []
        self.whites = []
        self.limit = 15

    def join_team(self, player):
        black = player[0]
        white = player[1]
        if black >= white:
            if len(self.blacks) < self.limit:
                hq.heappush(self.blacks, [black, -white])
            else:
                if self.blacks[0][0] < black:
                    p_black, p_white = hq.heappop(self.blacks)
                    hq.heappush(self.blacks, [black, -white])
                    if len(self.whites) < self.limit:
                        hq.heappush(self.whites, [-p_white, -p_black])
                    else:
                        if self.whites[0][0] < -p_white:
                            hq.heappush(self.whites, [-p_white, -p_black])
                        elif self.whites[0][0] == -p_white and self.whites[0][1] > -p_black:
                            hq.heappush(self.whites, [-p_white, -p_black])
                elif self.blacks[0][0] == black and self.blacks[0][1] > -white:
                    p_black, p_white = hq.heappop(self.blacks)
                    hq.heappush(self.blacks, [black, -white])
                    if len(self.whites) < self.limit:
                        hq.heappush(self.whites, [-p_white, -p_black])
                    else:
                        if self.whites[0][0] < -p_white:
                            hq.heappush(self.whites, [-p_white, -p_black])
                        elif self.whites[0][0] == -p_white and self.whites[0][1] > -p_black:
                            hq.heappush(self.whites, [-p_white, -p_black])
        else:
            if len(self.whites) < self.limit:
                hq.heappush(self.whites, [white, -black])
            else:
                if self.whites[0][0] < white:
                    p_white, p_black = hq.heappop(self.whites)
                    hq.heappush(self.whites, [white, -black])
                    if len(self.blacks) < self.limit:
                        hq.heappush(self.blacks, [-p_black, -p_white])
                    else:
                        if self.blacks[0][0] < -p_black:
                            hq.heappush(self.blacks, [-p_black, -p_white])
                        elif self.blacks[0][0] == -p_black and self.blacks[0][1] > -p_white:
                            hq.heappush(self.blacks, [-p_black, -p_white])
                elif self.whites[0][0] == white and self.whites[0][1] > -black:
                    p_white, p_black = hq.heappop(self.whites)
                    hq.heappush(self.whites, [white, -black])
                    if len(self.blacks) < self.limit:
                        hq.heappush(self.blacks, [-p_black, -p_white])
                    else:
                        if self.blacks[0][0] < -p_black:
                            hq.heappush(self.blacks, [-p_black, -p_white])
                        elif self.blacks[0][0] == -p_black and self.blacks[0][1] > -p_white:
                            hq.heappush(self.blacks, [-p_black, -p_white])

    def get_total(self):
        ans = 0
        for i in range(self.limit):
            ans += self.blacks[i][0] + self.whites[i][0]
        return ans


def solution():
    chessteam = ChessTeam()
    for p in sys.stdin.readlines():
        player = list(map(int, p.split()))
        chessteam.join_team(player)
    print(chessteam.get_total())


if __name__ == '__main__':
    solution()