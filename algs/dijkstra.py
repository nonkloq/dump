import heapq as hq 

INF = float('inf')
class Graph:
    def __init__(self,vertices):
        self.V = list(range(vertices))
        self.W = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edges(self,u,V,W):
        for i in range(len(V)):
            self.W[u][V[i]] = W[i]


def dijkstra(graph,source):
    Q = []
    
    Dist = [INF]*len(graph.V)
    Path = [None]*len(graph.V)

    for v in graph.V:
        if v == source: hq.heappush(Q,(0,v))
        hq.heappush(Q,(Dist[v],v))
        
    Dist[source] = 0
    visited = [False]*len(graph.V)
    
    for _ in range(len(graph.V)-1):
        _,u = hq.heappop(Q)
        if visited[u]: continue # since we not removing the old values
        else: visited[u] = True
        for v in graph.V:
            if (graph.W[u][v] > 0 and not visited[v]):
                if Dist[u] + graph.W[u][v] < Dist[v]:
                    Dist[v] = Dist[u] + graph.W[u][v]
                    Path[v] = u
                    hq.heappush(Q,(Dist[v],v))

    return Dist,Path

G = Graph(5)
V = {0:'a',1:'b',2:'c',3:'d',4:'e'}

G.add_edges(0,[1,3],[3,7])
G.add_edges(1,[0,2,3],[3,4,2])
G.add_edges(2,[1,3,4],[4,5,6])
G.add_edges(3,[0,1,2,4],[7,2,5,4])
G.add_edges(4,[2,3],[6,4])

source = 0
Dist,Path = dijkstra(G,source)


def printpath(u,v):
    if u == v: return
    x = v
    s = [V[v]]
    while Path[v]!=None:
        s.append(V[Path[v]])
        v = Path[v]
    s = s[::-1]
    print(f"from {V[u]} to {V[x]}: {'-'.join(s)}\tof length {Dist[x]}")
    
    
for v in G.V:
    printpath(source,v)