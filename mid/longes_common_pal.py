def longestPalindromicSubstring(string):
    m = [[0 for c in string] for x in string]
    pal = string[0]
    for i in range(len(string)):
        m[i][i] = 1

    for i in range(len(string) - 1):
        if string[i + 1] == string[i]:
            if 2 > len(pal):
                pal = string[i:i+2]

        m[i][i + 1] = 1 if string[i + 1] == string[i] else 0

    j = 2

    for i in m:
        print(i)

    while j < len(string):
        max_i = len(string) - j
        current_j = j
        for i in range(max_i):
            # if current_j == 5 and i == 1:
            #    print(string[i] , string[current_j], string[i + 1], string[current_j - 1], i, current_j)
            if string[i] == string[current_j] and m[i + 1][current_j - 1] > 0:
                m[i][current_j] = 2 + m[i + 1][current_j - 1]
                candidate = string[i: current_j + 1]
                if len(candidate) > len(pal):
                    pal = string[i: current_j + 1]

            else:
                m[i][current_j] = 0
            current_j += 1
        j = j + 1

    return pal



print(longestPalindromicSubstring("baa"))
# print(longestPalindromicSubstring("efghfe"))
# print(longestPalindromicSubstring("high"))
# print(longestPalindromicSubstring("axabaxac"))
# print(longestPalindromicSubstring("asdabbadx"))







