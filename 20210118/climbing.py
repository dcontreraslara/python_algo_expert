def climbingLeaderboard(ranked, player):
    # Write your code here
    res = [0 for x in player]
    ranked = ranked + [0]
    rr = {}
    rank = 1
    prev = ranked[0]
    for i in range(len(ranked)):
        if prev > ranked[i]:
            rank += 1
        prev = ranked[i]
        rr[ranked[i]] = rank

    j = 0
    i = 0
    ranked = sorted(ranked)
    added = False
    while j < len(ranked) and i < len(player):
        if player[i] < ranked[j]:
            res[i] = rr[ranked[j-1]]
            i += 1
            added = True
        else:
            added = False
            j += 1
    while i < len(player):
        res[i] = 1
        i +=1

    return res

