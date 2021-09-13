def dfs_make_path(root, board, path_set):
    """
    from the starting path [(row, col)] for which root can be seat with 'S'
    dfs function will investigate all available seven seat combinations
    """
    path = [root]
    available = set()
    dfs(path, board, available)
    for a in available:
        if a not in path_set:
            path_set.add(a)


def dfs(path, board, available):
    """
    by appending all possible seats adjacent to selected seats that doesn't violate rule
    you get the 7 seats that satisfy condition
    """
    if len(path) == 7:
        available.add(tuple(sorted(path)))
        return
    candidates = get_candidates(path)
    for candidate in candidates:
        new_path = path[:]
        if candidate not in new_path:
            new_path.append(candidate)
            if check_dominance(new_path, board):
                dfs(new_path, board, available)
        else:
            return


def get_candidates(path):
    """
    get the seats adjacent to the seats selected previously
    """
    destinations = set()
    for now in path:
        destinations.update(((now[0] + 1, now[1]), (now[0], now[1] + 1), (now[0] - 1, now[1]), (now[0], now[1] - 1)))
    new = []
    for dest in destinations:
        if dest not in path and 0 <= dest[0] <= 4 and 0 <= dest[1] <= 4:
            new.append(dest)
    return new


def check_dominance(path, board):
    """
    investigate if currently selected combination of seats
    are dominant with 'S'
    """
    count = 0
    for seat in path:
        if board[seat[0]][seat[1]] == 'Y':
            count += 1
    return count < 4


def solution():
    path_set = set()
    board = [list(input()) for _ in range(5)]
    for row in range(5):
        for col in range(5):
            if board[row][col] == 'S':
                dfs_make_path((row, col), board, path_set)
    print(len(path_set))
    # print(path_set)


solution()

"""
input
YYYYY
SYSYS
YYYYY
YSYYS
YYYYY

output
2
{((1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)), 
((1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (3, 1))}
added case to understand easily
to look at it remove # at line 67
"""
