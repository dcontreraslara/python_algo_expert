def lcs(s1, s2):

    if len(s1) == 0:
        return 0
    if len(s2) == 0:
        return 0

    if s1[-1] == s2[-1]:
        return 1 + lcs(s1[:-1], s2[:-1])

    return max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))


a = [1,2,3,4,5]
print(a)