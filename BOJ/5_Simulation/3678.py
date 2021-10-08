class Tile:
    def __init__(self, resource, n=None, ne=None, se=None, s=None, sw=None, nw=None):
        """
        make a Tile class with six sides
        each direction variables points to its adjacent Tile
        ex) self.n = Tile(which is adjacent to upper side of this tile)

        self.resource means the resource that this tile have range 1~5
        """
        self.resource = resource
        self.n = n
        self.ne = ne
        self.se = se
        self.s = s
        self.sw = sw
        self.nw = nw


class Board:
    def __init__(self):
        """
        create Catan Board
        self.resource is the counter of resources on board

        self.now acts as pointer which points to the most recent tile generated on the board
        we create next tile based on this tile

        self.board_by_tile_index is the flattened representation of Catan board.
        each index means the order of generation and the value is the resource on that tile
        ex) self.board_by_tile_index[0] = 1, first tile has resource 1

        self.tiles_count counts the number of generated tiles on board
        """
        self.resource = {1: 1, 2: 0, 3: 0, 4: 0, 5: 0}
        self.now = Tile(1)
        self.board_by_tile_index = [0] * 11000
        self.board_by_tile_index[0] = 1
        self.tiles_count = 1

    def create_board(self):
        """
        create Catan board based on the rule
        layer_count is the distance from the Center starting point, Center's layer count is 0
        spirally generate tile in direction ne -> n -> nw -> sw -> s -> se -> ne
        """
        layer_count = 1
        while self.tiles_count < 10000:
            self.create_ne()
            for _ in range(layer_count - 1):
                self.create_n()
            for _ in range(layer_count):
                self.create_nw()
            for _ in range(layer_count):
                self.create_sw()
            for _ in range(layer_count):
                self.create_s()
            for _ in range(layer_count):
                self.create_se()
            for _ in range(layer_count):
                self.create_ne()
            layer_count += 1

    def get_resource(self, not_available):
        """
        select appropriate type of resource to be generated on the board
        input not_available contains resources that is placed on the adjacent tiles
        """
        candidate = 6
        temp_min = 20000
        for resource in self.resource:
            if resource in not_available:
                continue
            if self.resource[resource] < temp_min:
                candidate = resource
                temp_min = self.resource[resource]
        self.resource[candidate] += 1
        return candidate

    def create_ne(self):
        """
        create new Tile which is upper right to self.now Tile.
        you need to consider three tiles generally.
        but there are cases where you consider only one or two tiles.
        complex ifs are used in order to handle those cases
        """
        not_available = set()
        sw = self.now
        not_available.add(sw.resource)
        nw = self.now.n
        if nw:
            not_available.add(nw.resource)
            n = self.now.n.ne
            if n:
                not_available.add(n.resource)
        else:
            n = None
        resource = self.get_resource(not_available)
        new_tile = Tile(resource, sw=sw, nw=nw, n=n)
        sw.ne = new_tile
        if nw:
            nw.se = new_tile
            if n:
                n.s = new_tile
        self.now = new_tile
        self.board_by_tile_index[self.tiles_count] = resource
        self.tiles_count += 1

    def create_nw(self):
        not_available = set()
        se = self.now
        not_available.add(se.resource)
        s = self.now.sw
        if s:
            not_available.add(s.resource)
            sw = self.now.sw.nw
            if sw:
                not_available.add(sw.resource)
        else:
            sw = None
        resource = self.get_resource(not_available)
        new_tile = Tile(resource, se=se, s=s, sw=sw)
        se.nw = new_tile
        if s:
            s.n = new_tile
            if sw:
                sw.ne = new_tile
        self.now = new_tile
        self.board_by_tile_index[self.tiles_count] = resource
        self.tiles_count += 1

    def create_sw(self):
        not_available = set()
        ne = self.now
        not_available.add(ne.resource)
        se = self.now.s
        if se:
            not_available.add(se.resource)
            s = self.now.s.sw
            if s:
                not_available.add(s.resource)
        else:
            s = None
        resource = self.get_resource(not_available)
        new_tile = Tile(resource, ne=ne, se=se, s=s)
        ne.sw = new_tile
        if se:
            se.nw = new_tile
            if s:
                s.n = new_tile
        self.now = new_tile
        self.board_by_tile_index[self.tiles_count] = resource
        self.tiles_count += 1

    def create_s(self):
        not_available = set()
        n = self.now
        not_available.add(n.resource)
        ne = self.now.se
        if ne:
            not_available.add(ne.resource)
            se = self.now.se.s
            if se:
                not_available.add(se.resource)
        else:
            se = None
        resource = self.get_resource(not_available)
        new_tile = Tile(resource, n=n, ne=ne, se=se)
        n.s = new_tile
        if ne:
            ne.sw = new_tile
            if se:
                se.nw = new_tile
        self.now = new_tile
        self.board_by_tile_index[self.tiles_count] = resource
        self.tiles_count += 1

    def create_se(self):
        not_available = set()
        nw = self.now
        not_available.add(nw.resource)
        n = self.now.ne
        if n:
            not_available.add(n.resource)
            ne = self.now.ne.se
            if ne:
                not_available.add(ne.resource)
        else:
            ne = None
        resource = self.get_resource(not_available)
        new_tile = Tile(resource, nw=nw, n=n, ne=ne)
        nw.se = new_tile
        if n:
            n.s = new_tile
            if ne:
                ne.sw = new_tile
        self.now = new_tile
        self.board_by_tile_index[self.tiles_count] = resource
        self.tiles_count += 1

    def create_n(self):
        not_available = set()
        s = self.now
        not_available.add(s.resource)
        sw = self.now.nw
        if sw:
            not_available.add(sw.resource)
            nw = self.now.nw.n
            if nw:
                not_available.add(nw.resource)
        else:
            nw = None
        resource = self.get_resource(not_available)
        new_tile = Tile(resource, s=s, sw=sw, nw=nw)
        s.n = new_tile
        if sw:
            sw.ne = new_tile
            if nw:
                nw.se = new_tile
        self.now = new_tile
        self.board_by_tile_index[self.tiles_count] = resource
        self.tiles_count += 1


def solution():
    board = Board()
    board.create_board()
    ans = board.board_by_tile_index
    n = int(input())
    query = []
    for _ in range(n):
        query.append(int(input()))
    for q in query:
        print(ans[q-1])

solution()

"""
4
1
4
10
100

1
4
5
5
"""