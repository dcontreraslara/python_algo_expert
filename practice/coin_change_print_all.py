def coinChange(total, coins):
    if total == 0:
        return [[]]

    res = []
    for i in range(len(coins)):
        if total - coins[i] < 0:
            continue
        current_coin = coins[i]
        for out in coinChange(total - current_coin, coins):
            res.append([current_coin] + out)

    return res

print(coinChange(3,[1,2,3,4,5,6,7,8,9,10]))
print(coinChange(5,[1,2,3,4,5,6,7,8,9,10]))