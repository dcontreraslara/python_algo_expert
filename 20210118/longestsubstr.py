def longestSubstringWithoutDuplication(string):
    res = [0] * len(string)
    data = {string[0]: 0}
    res[0] = 1
    MVAL = [0, 0]
    current_start = 0
    if len(string) == 1:
        return string
    for i in range(1, len(string)):
        if string[i] not in data or current_start > data[string[i]]:
            data[string[i]] = i
            res[i] = res[i - 1] + 1
        else:
            res[i] = i - data[string[i]]
            current_start = data[string[i]] + 1
            data[string[i]] = i

        if MVAL[0] < res[i]:
            MVAL[0] = res[i]
            MVAL[1] = i

    start_idx = MVAL[1] + 1 - MVAL[0]
    print(res, MVAL, start_idx)
    return string[start_idx:start_idx + MVAL[0]]


print(longestSubstringWithoutDuplication("aa"))
print(longestSubstringWithoutDuplication("clementisacap"))