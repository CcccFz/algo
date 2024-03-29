class Graph:
    def __init__(self, n) -> None:
        self.n = n
        self.vertex = [[] for _ in range(n)]
    
    def add_edge(self, _from, to):
        if _from >= self.n or to >= self.n:
            return
        self.vertex[_from].append(to)

    def topo_sort_kahn(self):
        in_degree = [0] * self.n
        for tos in self.vertex:
            for to in tos:
                in_degree[to] += 1
        queue = [_from for _from in range(self.n) if in_degree[_from] == 0]
        while queue:
            _from = queue.pop(0)
            print(_from, end=' ')
            for to in self.vertex[_from]:
                in_degree[to] -= 1
                if in_degree[to] == 0:
                    queue.append(to)
        print()

    def topo_sort_dfs(self):
        reverse_vertex, visited = [[] for _ in range(self.n)], [False]*self.n
        for _from, tos in enumerate(self.vertex):
            for to in tos:
                reverse_vertex[to].append(_from)
        def dfs(_from):
            visited[_from] = True
            for to in reverse_vertex[_from]:
                if visited[to]:
                    continue
                dfs(to)
            print(_from, end=' ')
        for _from in range(self.n):
            if visited[_from]:
                continue
            dfs(_from)
        print()


graph = Graph(8)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(4, 2)
graph.add_edge(5, 6)
graph.add_edge(6, 7)

graph.topo_sort_kahn()
graph.topo_sort_dfs()

# 内裤: 0
# 裤子: 1
# 鞋子: 2
# 腰带: 3
# 袜子: 4
# 衬衣: 5
# 外套: 6
# 领带: 7

# 0 4 5 1 6 2 3 7
# 0 1 4 2 3 5 6 7
# 0 1 3 4 2 5 7 6
# 5 6 7 0 4 1 2 3