
INF = float("inf")

def Children(i,j): # generate n childrens
    k = i+(j-i)//2
    return [
        ('left',(i,k)),
        ('right',(k+1,j))
        ]

def ABsearch(state,a,b,ismax=True):
    if state[0] == state[1]: 
        return Utility[state[0]],None
    m = None
    if ismax:
        v = -INF 
        for action,child in Children(*state):
            v2,m2 = ABsearch(child,a,b,False)
            if v2 > v:
                v,m = v2,action 
                a = max(a,v)
            if a >= b: break # comment this line to switch to normal Minimax
    else:
        v = INF
        for action,child in Children(*state):
            v2,m2 = ABsearch(child,a,b,True)
            if v2 < v:
                v,m = v2,action
                b = min(b,v)
            if a >= b: break # comment this line to switch to normal Minimax
    return v,m


Utility = [1,1,-1,1,0,0,-1,0,1,-1,-1,0,-1,0,1,-1,1,1,1,-1,1,0] 

start = (0,len(Utility)-1)
v,action = ABsearch(start,-INF,INF)
print(f"Moving to {action} yields the best score {v}")
