def appendAndDelete(s, t, k, d= {}):
    kk = s + "-" + t + "-" + str(k)
    if kk in d:
        return d[kk]

    if len(s) + len(t) + 1 == k:
        return "Yes"
    elif len(s) >0 and s == t and k == 0:
        return "Yes"
    elif k <= 0:
        return "No"

    A , B , C , D = "", "", "", ""
    if len(t) > 0:
        A = appendAndDelete(s+t[-1], t, k -1)
        D = appendAndDelete(s, t[:-1], k - 1)
    if len(s) > 0:
        B = appendAndDelete(s,t+s[-1], k -1)
        C = appendAndDelete(s[:-1], t, k - 1)


    d[kk] = max(A, B, C, D)
    return d[kk]






print(appendAndDelete("aba", "aba", 7))
print(appendAndDelete("ashley", "ashl", 2))
print(appendAndDelete("aaa", "a", 5))
print(appendAndDelete("aaaaaaaaaa", "aaaaa", 7))
print(appendAndDelete("hackerhappy", "hackerrank", 9))
print(appendAndDelete("qwerty", "zxcvbn", 9))
