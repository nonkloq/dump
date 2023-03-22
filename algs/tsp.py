from heapq import heappush, heappop
from collections import defaultdict
import math 

INF = float('inf')

class Graph:
    def __init__(self,vertices):
        self.V = list(range(vertices))
        self.W = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edges(self,u,V,W):
        for i in range(len(V)):
            self.W[u][V[i]] = W[i]

class Node:
    def __init__(self,path,i,lb):
        self.path = path 
        self.i = i
        self.lb = lb
    
    def __lt__(self,right):
        return self.lb < right.lb 


def getNearestTwo(v,G):
    a,b = INF,INF
    for w in G.W[v]:
        if w == 0: continue
        if w < a: a,b =w,a 
        elif w < b: b =w
    return a,b

def getNearest(v,G,u):
    a = INF
    wt = G.W[v]
    for i in range(len(wt)):
        if wt[i] == 0 or i == u: continue
        if wt[i] < a: a = wt[i] 
    return a

def lowerbound(G,path):
    s = 0
    include = defaultdict(list)
    for k,v in path.items():
        include[k].append(v)
        include[v].append(k) 
    
    for v in G.V:
        if v in include:
            if len(include[v])==1:
                u = include[v][0]
                a = G.W[v][u]
                b = getNearest(v,G,u)
            else: a,b = G.W[v][include[v][0]],G.W[v][include[v][1]]
        else: a,b = getNearestTwo(v,G)
        s +=(a+b)
    
    return math.ceil(s/2)


def tspBB(G,source):
    N = len(G.V)
    Q = []
    start = Node({},source,lowerbound(G,{}))
    heappush(Q,start)

    optimal = (None,INF)

    while Q:
        node = heappop(Q)
        lb, path , i = node.lb,node.path,node.i
        
        if len(path)==N:
            if lb<optimal[1]: optimal = (path,lb)
            continue
         
        if lb >= optimal[1]: continue
        

        for v in G.V:
            if v == i or v in path: continue
            
            new_path = dict(path)
            new_path[i] = v
            if len(new_path) == N-1:
                new_path[v] = source
            new_node = Node(new_path,v,lowerbound(G,new_path))
            heappush(Q,new_node)
    
    return optimal

G = Graph(5)
V = {0:'a',1:'b',2:'c',3:'d',4:'e'}
G.add_edges(0,[1,2,3,4],[3,1,5,8])
G.add_edges(1,[0,2,3,4],[3,6,7,9])
G.add_edges(2,[0,1,3,4],[1,6,4,2])
G.add_edges(3,[0,1,2,4],[5,7,4,3])
G.add_edges(4,[0,1,2,3],[8,9,2,3])
source = 0

path,cost = tspBB(G,source)

def printpath(path,source):
    out = f"{V[source]}-"
    u = path[source]
    while source != u:
        out += f"{V[u]}-"
        u = path[u]
    out += V[u]
    return out
print("Optimal Path:",printpath(path,0),"of cost",cost)