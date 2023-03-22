from queue import PriorityQueue
from random import random

N = 3
key = lambda i, j: i*N+j
rev = lambda x: (x//N,x%N)

def F(d,board):
    cost = 0

    if heuristics == "man":
        # Manhattan Distance
        for x in range(len(board)):
            c_i, c_j = rev(x)
            g_i, g_j = rev(board[x])
            cost += ((g_i-c_i)**2 + (g_j-c_j)**2)

    if heuristics == "mis":
        # Wrong tile
        for x in range(len(board)):
            if x != board[x]: cost+=1
    print(d,cost)
    return d + cost 


def children(d,board,path):
    x = path[-1]
    i,j = rev(x)
    for k,l in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        if 0<=k<N and 0<=l<N:
            y=key(k,l)
            board[x],board[y] = board[y],board[x]
            new_board = tuple(board)
            if new_board not in history:
                cost = F(d, board)
                
                Q.put((cost,(d,new_board,path+[y])))
                history.add(new_board)

            board[x],board[y] = board[y],board[x]


def solve(d,board,path)-> list:
    Q.put((0,(d,board,path)))
    while not Q.empty():
        cost, items = Q.get()
        d, board, path = items
        if board == (0,1,2,3,4,5,6,7,8): return cost,path    
        children(d+1,list(board),path)
    

    return None

    

Q = PriorityQueue()
history = set()
board = [
    3,1,2,
    4,7,5,
    6,8,0,
    ]
heuristics = "man" #"man","mis",""

path = solve(0,tuple(board), [8])

if path == None: print("The Given State is not Solvable!")
else: print(f"The Path is: {path[1]}\nThe Cost is: {path[0]}")
