def DFS(time, profit):
    global max_profit

    if time == n+1:
        if profit > max_profit:
            max_profit = profit
        return
    else:
        if time+time_li[time] <= n+1:
            DFS(time + time_li[time], profit + profit_li[time])
        DFS(time+1, profit)


if __name__ == "__main__":
    n = int(input())
    time_li = []
    profit_li = []
    max_profit = 0

    for _ in range(n):
        a,b = map(int, input().split())
        time_li.append(a)
        profit_li.append(b)

    time_li.insert(0,0)
    profit_li.insert(0,0)

    DFS(1, 0)
    print(max_profit)