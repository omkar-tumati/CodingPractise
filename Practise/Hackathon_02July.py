def ProfitofMeger(N,plots,cost):
    sum = 0
    price = 0
    for i in range(0,N):
        price = price + (plots[i] * cost[i])
        for j in range(i+1):
            if(i>0):
                sum = sum + plots[j]
    if price > sum:
        print("Profit")
    elif price < sum:
        print("Loss")
    print(sum,price)
    
if __name__ == "__main__":
    N = 5
    plots = [10, 20, 35, 70, 150]
    cost = [2, 4, 6, 1, 3]
    ProfitofMeger(N, plots, cost)