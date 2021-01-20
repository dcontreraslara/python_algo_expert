def can_put(bot, top):
    if bot[0] > top[0] and bot[1] > top[1] and bot[2] > top[2]:
        return True
    return False


def diskStacking(disks):

    if len(disks) == 1:
        return disks

    disks.sort(key=lambda d: d[2], reverse=True)
    print(disks)
    result = [x[2] for x in disks]
    values = [x for x in range(len(disks))]

    max_value = (-1, -1)
    for i in range(len(disks)):
        j = 0

        if max_value[0] < result[i]:
            max_value = (result[i], i)

        while j < i:
            if(can_put(disks[j], disks[i])):
                if (result[j] + disks[i][2]) > result[i]:
                    result[i] = result[j] + disks[i][2]
                    values[i] = j
                    if max_value[0] < result[i]:
                        max_value = (result[i], i)
            j = j + 1

    j = max_value[1]
    res = []
    prev = -1
    while j != prev:
        res.append(disks[j])
        prev = j
        j = values[j]
    return res




ii = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
print(diskStacking(ii))