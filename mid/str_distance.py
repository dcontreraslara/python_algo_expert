def levenshteinDistance(str1, str2, d={}):

    key = str1 + "..." + str2

    if key in d:
        return d[key]

    if len(str1) == 0 and len(str2) > 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)

    val = None
    if str1[0] == str2[0]:
        val = levenshteinDistance(str1[1:], str2[1:])
    else:
        val = 1 + min(levenshteinDistance(str1[1:], str2),
                       levenshteinDistance(str1, str2[1:]),
                       levenshteinDistance(str1, str1[0] + str2[1:]))

    d[key] = val
    return val


print(levenshteinDistance("abc", "yabd"))