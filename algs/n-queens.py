def isValid(board,i,j):
    n = len(board)    
    k = i-1
    a,b = j-1,j+1

    while 0<=k:
        if board[k][j]: return False
        if 0<=a:
            if board[k][a]: return False
            a-=1
        if b<n:
            if board[k][b]: return False
            b+=1
        k-=1

    return True

def backtrack(board,i):
    n = len(board)
    if i>=n: return True

    for j in range(n):
        if isValid(board,i,j): 
            board[i][j] = 1

            if backtrack(board,i+1): return True 
            
            board[i][j] = 0
    
    return False

def nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    backtrack(board,0)
    return board


N = 10
for r in nqueens(N):
    print(r)