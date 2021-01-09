def numberOfWaysToMakeChange(n, denoms):
    if n < 0 or len(denoms) == 0:
        return 0

    if n == 0:
        return 1

    change = numberOfWaysToMakeChange(n - denoms[0], denoms) + numberOfWaysToMakeChange(n, denoms[1:])

    return change
