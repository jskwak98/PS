def decide_under(top, board):
    """
    :param top: upper row index list ((0,0),(0,1),(0,2),(0,3),(0,4)) for n=5
    :param board: board made so far
    :return:
    """
    board.append(["#" if odd_black(tile, board) else "." for tile in top])
    print("".join(board[-1]))


def odd_black(tile, board):
    """
    :param tile: index of specific tile ex : (2,2)
    :param board: board made so far
    :return: True if there are 1 or 3 # adjacent to the tile given as input else False
    """
    count = 0
    if tile[0] != 0:  # up
        count += board[tile[0]-1][tile[1]] == "#"
    if tile[1] > 0:  # left
        count += board[tile[0]][tile[1]-1] == "#"
    if tile[1] < len(board[0])-1:  # right
        count += board[tile[0]][tile[1]+1] == "#"
    return count % 2 == 1


def solution():
    n = int(input())
    first_row = list(input())
    print("".join(first_row))
    board = [first_row]
    for row in range(n-1):
        decide_under(tuple(zip([row]*n, range(n))), board)


solution()
