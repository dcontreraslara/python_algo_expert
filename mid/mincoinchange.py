
def minNumberOfCoinsForChange(n, denoms):

    m = [[0 for x in range(n +1)] for row in range(len(denoms))]
    i = 0
    j = 0

    sorted(denoms)
    coin_value = denoms[0]
    # base case
    while j < len(m[0]):
        if j % coin_value == 0:
            m[0][j] = j // coin_value
        else:
            m[0][j] = -1
        j = j + 1

    # 0 coin change base case
    while i < len(m):
        m[i][0] = 0
        i = i + 1

    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            coin_value = denoms[i]
            # print(j, coin_value)
            if j - coin_value < 0:
                m[i][j] = m[i-1][j]
            else:
                new_idx = j - coin_value
                total_coins = (1 + m[i][new_idx]) if m[i][new_idx] != -1 else -1

                if total_coins == -1:
                    m[i][j] = m[i-1][j]
                elif m[i-1][j] == -1:
                    m[i][j] = total_coins
                else:
                    m[i][j] = min(m[i-1][j], total_coins)
    for i in m:
        print(i)
    return m[len(m)-1][n]



print(minNumberOfCoinsForChange(7, [3, 7]))
print(minNumberOfCoinsForChange(7, [2, 4]))
print(minNumberOfCoinsForChange(7, [1, 5, 10]))
print(minNumberOfCoinsForChange(18, [1, 5, 10]))