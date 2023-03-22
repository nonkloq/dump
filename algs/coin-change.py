def getchange(coins,money):
    n = len(coins)
    D = [[0 for _ in range(n)] for _ in range(money+1)]
    
    for i in range(n):
        D[0][i] = 1
    
    for i in range(1,money+1):
        for j in range(n):
            a = D[i - coins[j]][j] if i-coins[j]>=0 else 0
            b = D[i][j-1] if j>=1 else 0

            D[i][j] = a+b

    return D[money][n-1]

coins = [2,8,5,9,10]
money = 10
print(f"Coins: {coins}, Money: {money}")
print("No. of ways for change:",getchange(coins,money))