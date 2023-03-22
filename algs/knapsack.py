def knapsack(W, weight, value): 
    n=len(value)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(W + 1): 
            if i == 0 or j == 0: table[i][j] = 0
            elif weight[i-1] <= j: table[i][j] = max(value[i-1] + table[i-1][j-weight[i-1]],  table[i-1][j]) 
            else: table[i][j] = table[i-1][j] 
   
    return table[n][W] 
    
value = [12,10,20,15] 
weight = [2,1,3,2] 
W = 5 # Capacity
 
print(knapsack(W, weight, value))
