from queue import PriorityQueue

# heuristic function
def F(steps,curr,dest):
    return steps + abs(dest[0]-curr[0])+abs(dest[1]-curr[1])   

# children state generator
def generateChildrens(m,n,maze,i,j):
    for a,b in (i,j-1),(i,j+1),(i-1,j),(i+1,j):
        if 0<=a<m and 0<=b<n and maze[a][b] != 1: yield (a,b)


def AstarSearch(maze,start,dest):
    m, n = len(maze),len(maze[0])
    
    expanded = set()
    Q = PriorityQueue()
    Q.put((0,(0,start)))
    while Q.qsize():
        value, node = Q.get()
        steps, curr = node
        if curr == dest: return steps
        expanded.add(curr)

        for children in generateChildrens(m,n,maze,*curr):
            if children in expanded: continue # no uturns
            Q.put(
                (
                    F(steps+1,children,dest),
                    (steps+1,children)
                )
            )
    return None


maze = [[0,0,0,0,0,0],
        [0,1,1,1,1,0],
        [0,1,0,0,0,0],
        [0,1,1,0,1,1],
        [1,0,0,0,0,0]]

dest = (0,0)
start = (len(maze)-1,len(maze[0])-1)

steps = AstarSearch(maze,start,dest)

if steps: print(f"A* search took {steps} steps to reach the target")
else: print("Path doesn't exist")