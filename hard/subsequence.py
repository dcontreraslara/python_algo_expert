def longestCommonSubsequence(str1, str2, d={}, val={}):
    key = (str1,str2)
    if len(str1) <= 0 or len(str2) <= 0:
        return []

    if key in d:
        return d[key]

    if str1[len(str1) - 1] == str2[len(str2) - 1]:
        d[key] = longestCommonSubsequence(str1[:len(str1) - 1], str2[:len(str2) - 1]) + [str1[len(str1)-1]]
        return d[key]

    left = longestCommonSubsequence(str1[:len(str1) - 1], str2)
    right = longestCommonSubsequence(str1, str2[:len(str2) - 1])

    if len(left) > len(right):
        d[key] = left
    else:
        d[key] = right
    return d[key]


print(longestCommonSubsequence("ZXVVYZW", "XKYKZPW"))