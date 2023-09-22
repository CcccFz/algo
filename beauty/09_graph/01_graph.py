class Graph:
    def __init__(self):
        self.vertex = []

    def add_edge(self, _from, to):
        while len(self.vertex)-1 < _from or len(self.vertex)-1 < to:
            self.vertex.append([])
        self.vertex[_from].append(to)
        self.vertex[to].append(_from)  # 没有此句，则为有向图
    
    def bfs(self, _from, to):
        if _from == to:
            return [_from]

        ret = []
        visited = [False] * len(self)
        prev = [None] * len(self)

        visited[_from] = True
        queue = [_from]
        while queue:
            i = queue.pop(0)
            for j in self.vertex[i]:
                if visited[j]:
                    continue
                prev[j] = i
                if j == to:
                    ret.insert(0, j)
                    while prev[j] is not None:
                        ret.insert(0, prev[j])
                        j = prev[j]                        
                    return ret                
                queue.append(j)
                visited[j] = True
        
        return ret

    def find_vertex_at_degree(self, _from, degree):
        if degree == 0:
            return [_from]

        ret = []
        visited = [False] * len(self)

        visited[_from] = True
        queue = [_from]
        while queue:
            for _ in range(len(queue)):
                i = queue.pop(0)
                for j in self.vertex[i]:                
                    if visited[j]:
                        continue
                    queue.append(j)
                    visited[j] = True
            degree -= 1
            if degree == 0:
                ret = list(queue)
                break

        return ret

    def dfs(self, _from, to):
        def _dfs(_from):
            nonlocal found
            visited[_from] = True
            if found:
                return
            if _from == to:
                found = True
                ret.insert(0, _from)
                while prev[_from] is not None:
                    _from = prev[_from]
                    ret.insert(0, _from)
                return

            for i in self.vertex[_from]:
                if visited[i]:
                    continue
                prev[i] = _from
                _dfs(i)

        if _from == to:
            return [_from]
        
        ret = []
        visited = [False] * len(self)
        prev = [None] * len(self)
        found = False

        _dfs(_from)
        return ret

    def __len__(self):
        return len(self.vertex)

    def __repr__(self) -> str:
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
    print(graph.find_vertex_at_degree(0, 3)) # 3:5,6 4:7
    print(graph.dfs(0, 7))  # [0, 1, 2, 5, 4, 6, 7]