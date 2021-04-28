class Graph:
    edges =[]
    dfs_tree = []
    bfs_tree = []

    def __init__(self, raw_edges, convert_down):
        if convert_down:
            temp = []
            for e in raw_edges:
                temp.append((e[0]-1, e[1]-1))
            raw_edges = temp
        max_vertex = 0
        for edge in raw_edges:
            max_vertex = max(max_vertex, max(edge[0], edge[1]))
        self.edges = [[False for y in range(max_vertex+1)] for x in range(max_vertex+1)]
        self.found = [False for x in range(len(self.edges))]

        for e in raw_edges:
            self.edges[e[0]][e[1]] = True
        print("edges: ")
        for row in self.edges:
            print(row)
        print()

    def dfs(self, start_vertex, convert_down):
        print("dfs: ")
        stack = []
        self.found = [False for x in range(len(self.edges))]
        stack.insert(0,start_vertex)
        while len(stack) != 0 and not self.done():
            cur = stack.pop(0)
            if convert_down: print("found: ", cur + 1) 
            else: print("found: ", cur)
            self.found[cur] = True
            for vertex, edge in enumerate(reversed(self.edges[cur])):
                if edge and not self.found[vertex]:
                    stack.insert(0,vertex)
                    if convert_down: self.dfs_tree.append((cur+1,vertex+1))
                    else: self.dfs_tree.append((cur,vertex))
        print()
    def bfs(self, start_vertex, convert_down):
        print("bfs: ")

        queue = []
        self.found = [False for x in range(len(self.edges))]
        queue.append(start_vertex)
        while len(queue) != 0 and not self.done():
            cur = queue.pop(0)
            if convert_down: print("found: ", cur + 1) 
            else: print("found: ", cur)
            self.found[cur] = True
            for vertex, edge in enumerate(self.edges[cur]):
                if edge and not self.found[vertex] and vertex not in queue:
                    queue.append(vertex)
                    if convert_down: self.bfs_tree.append((cur+1,vertex+1))
                    else: self.bfs_tree.append((cur,vertex))
        print()

    def done(self):
        for f in self.found:
            if not f:
                return False
        return True
    
    def print_trees(self):
        print("print_dfs_tree:")
        self.dfs_tree.sort()
        for edge in self.dfs_tree:
            print(edge)
        print()
        
        print("print_bfs_tree:")
        self.bfs_tree.sort()
        for edge in self.bfs_tree:
            print(edge)
        print()


raw_input_edges = [(10,9),(9,3),(2,9),(8,9), (3,2),(1,2),(1,0),(0,5), (4,5),(4,3),(0,4),(8,1),(7,8),(7,12), (12,11),(11,10), (10,11),(5,12),(12,0), (1,7)]
g = Graph(raw_input_edges, False)
g.dfs(0, False)
# g.bfs(0, False)
g.print_trees()



