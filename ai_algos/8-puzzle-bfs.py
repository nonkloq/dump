N = 3
key = lambda i, j: i*N+j
rev = lambda x: (x//N,x%N)

def children(board,path,history):
    x = path[-1]
    i,j = rev(x)
    out = []
    for k,l in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        if 0<=k<N and 0<=l<N:
            y=key(k,l)
            board[x],board[y] = board[y],board[x]
            new_board = tuple(board)
            board[x],board[y] = board[y],board[x]

            if new_board not in history: 
                history.add(new_board)
                out += [(new_board,path+[y])]
    return out

def solve(board,path)-> list:
    Q = [(board,path)]
    history = set()
    while Q:
        n = len(Q)
        board,path = Q.pop(0)
        if board == goal_state: return path
        Q+= children(list(board), path,history)
    return None

    
board = [
    3,1,2,
    4,7,5,
    6,8,0,
    ]
goal_state = (0,1,2,3,4,5,6,7,8)
path = solve(board, [8])
if path == None: print("The Given State is not Solvable!")
else: print(f"The Path is: {path}\nThe Cost is: {len(path)-1}")
