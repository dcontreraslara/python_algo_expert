def coinChange(total, coins, res=[]):

    if total == 0:
        return 0, []

    if total < 0 or len(coins) == 0:
        return -1, []

    t1, u1 = coinChange(total - coins[0], coins)
    u1 = u1 + [coins[0]]

    t2, u2 = coinChange(total, coins[1:])

    if t1 == t2 == 0:
        if len(u1) < len(u2):
            return t1, u1
        return t2, u2
    if t1 == 0:
        return t1, u1

    return t2, u2


c= [1, 2, 3, 5, 10]
print(coinChange(10, c))
print(coinChange(16, c))


