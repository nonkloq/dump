from queue import PriorityQueue
INF = float('inf')

def upperbound(W,w,v,r):
    return -1*(v + (W-w) * r)

def maketable(weights,values):
    table = []
    for w,v in zip(weights,values):
        table.append((w,v,v/w))
    return sorted(table,reverse=True,key= lambda row: row[2])


def knapsackBB(W,weights,values):
    """With without branch and bound"""
    table = maketable(weights,values)
    n = len(table)
    optimal = (None,-INF) 

    Q = PriorityQueue()

    Q.put(
            (
            upperbound(W,0,0,table[0][2]),
            (0,0,0)
            )
        )

    
    while Q.qsize()>0:
        ub, wvk = Q.get()
        w,v,k = wvk
        
        if (-1*ub) <= optimal[1]: continue # if upperbound lesser than optimal value

        if k==n or w == W: # if capacity reached or no elements available
            if v>optimal[1]: optimal = (w,v)
            continue

        wk,vk,rk = table[k]
        if k+1 < n:
            _,_,rk = table[k+1]
        else: rk=INF # if last element

        # with k
        if w+wk<=W: # feasible check
            new_ub = upperbound(W,w+wk,v+vk,rk) 
            Q.put((new_ub,(w+wk,v+vk,k+1)))
        # without k
        new_ub = upperbound(W,w,v,rk)
        Q.put((new_ub,(w,v,k+1)))
    
    return optimal




W = 10
weights = [4,7,5,3]
values = [40,42,25,12]

print("Optimal Solution (weight,value):", knapsackBB(W,weights,values))