class GraphMaker:
    """
    Based on the input, it makes a graph
    which uses binary codes as nodes,
    hamming distance as edges.

    :param n: number of nodes
    :param data: input data which will be used to make nodes and edges
                 concatenated '3' as prefixes for convention
    """

    def __init__(self, n, data):
        self.n = n
        self.data = data
        self.mat = self.make_mat()
        self.path = None
        self.found = False

    def make_mat(self):
        mat = [[0] * self.n for _ in range(self.n)]
        for node_i in range(self.n - 1):
            for code_i in range(node_i + 1, self.n):
                hd = self.hamming_dist(self.data[node_i], self.data[code_i])
                mat[node_i][code_i] = hd
                mat[code_i][node_i] = hd
        return mat

    def hamming_dist(self, node, code):
        """
        add two numbers and count number of '1' which can
        only be result of two different numbers in same digits
        """
        return int(str(int(node) + int(code)).count('1') == 1)

    def dist(self, root, dest):
        visited = [False] * self.n
        path = []
        self.dfs(root, dest, visited, path)
        if self.found:
            print(" ".join(self.path))
        else:
            print(-1)

    def dfs(self, root, dest, visited, path):
        """
        perform dfs while recording the path current
        recursion had went through
        :param root: actually, it means parent not root
        :param dest: destination from query input
        :param visited: visited list, but it is recorded separately by recursion
        :param path: path that current recursion had went through
        :return:
        """
        if self.found:
            return
        local_path, local_visited = path[:], visited[:]
        local_path.append(str(root + 1))
        local_visited[root] = True
        if root == dest:
            self.path = local_path
            self.found = True
            return
        else:
            for node_i in range(self.n):
                if self.mat[root][node_i] and not local_visited[node_i]:
                    self.dfs(node_i, dest, local_visited, local_path)
            return


def solution():
    n, _ = map(int, input().split())
    data = ['3' + input() for _ in range(n)]
    root, dest = map(int, input().split())
    gm = GraphMaker(n, data)
    gm.dist(root - 1, dest - 1)


solution()

"""
5 3
000
111
010
110
001
1 2

1 3 4 2
"""