class Graph:
    def __init__(self, vertices):
        self.V = range(1,vertices+1)
        self.E = {u :[] for u in self.V}

    def add_edges(self,u,v):
        if u<=0  or u>self.V[-1]: return
        self.E[u] += v

def DFStraverse(graph,visited,stack, u):
    visited.add(u)

    for v in graph.E[u]:
        if v not in visited:
            DFStraverse(graph, visited, stack, v)
    stack.append(u)


def topologicalsortDFS(graph):
    stack = []
    visited = set()

    for u in graph.V:
        if u not in visited:
            DFStraverse(graph,visited,stack, u)
    
    return stack[::-1]

def topologicalsortSourceRemoval(graph):
    in_degree = [0]*(len(graph.V)+1)

    for u in graph.V:
        for v in graph.E[u]:
            in_degree[v]+=1
    
    Q = [u for u in graph.V if in_degree[u] == 0]

    order = []
    while Q:
        u = Q.pop(0)
        for v in graph.E[u]:
            in_degree[v]-=1
            if in_degree[v] == 0: Q.append(v)
        order.append(u)
    
    return order
G = Graph(5)
G.add_edges(1,[3])
G.add_edges(2,[3])
G.add_edges(3,[4,5])
G.add_edges(4,[5])
G.add_edges(5,[])

print("DFS Algorithm: ",topologicalsortDFS(G))
print("Source Removal: ",topologicalsortSourceRemoval(G))