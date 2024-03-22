class Graph:
    def __init__(self):
        self.vertex = []

    def add_edge(self, _from, to):
        while len(self) <= max(_from, to):
            self.vertex.append([])
        self.vertex[_from].append(to)
        self.vertex[to].append(_from)

    def bfs(self, _from, to):
        if _from == to:
            return [to]
        prev, visited, queue = [None]*len(self), [False]*len(self), [_from]
        visited[_from] = True
        while queue:
            i = queue.pop(0)
            for j in self.vertex[i]:
                if visited[j]:
                    continue
                visited[j], prev[j] = True, i
                if j == to:
                    ret = [to]
                    while prev[j] is not None:
                        ret.insert(0, prev[j])
                        j = prev[j]
                    return ret
                queue.append(j)

    def find_vertex_at_degree(self, _from, degree):
        if degree == 0:
            return [_from]
        visited, queue, ret = [False]*len(self), [_from], []
        visited[_from] = True
        while queue:
            degree -= 1
            for _ in range(len(queue)):
                i = queue.pop(0)
                for j in self.vertex[i]:
                    if visited[j]:
                        continue
                    visited[j] = True
                    ret.append(j)
                    queue.append(j)
            if degree == 0:
                break
        return ret

    def dfs(self, _from, to):
        def _dfs(i):
            nonlocal found
            if found:
                return
            visited[i] = True
            if i == to:
                ret.append(to)
                while prev[i] is not None:
                    ret.insert(0, prev[i])
                    i = prev[i]
                found = True
                return
            for j in self.vertex[i]:
                if visited[j]:
                    continue
                prev[j] = i
                _dfs(j)

        ret, found, visited, prev = [], False, [False]*len(self), [None]*len(self)
        _dfs(_from)
        return ret

    def __len__(self):
        return len(self.vertex)

    def __repr__(self):
        for i, vertex in enumerate(self.vertex):
            print(i, vertex)
        return ''


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)
    print(graph)
    print(graph.bfs(0, 7))    # [0, 1, 2, 5, 7]
    print(graph.find_vertex_at_degree(0, 3))  # 4度多个7
    print(graph.dfs(0, 7))  # [0, 1, 2, 5, 4, 6, 7]


# 0 [1, 3]
# 1 [0, 2, 4]
# 2 [1, 5]
# 3 [0, 4]
# 4 [1, 3, 5, 6]
# 5 [2, 4, 7]
# 6 [4, 7]
# 7 [5, 6]

# [0, 1, 2, 5, 7]
# [1, 3, 2, 4, 5, 6]
# [0, 1, 2, 5, 4, 6, 7]
