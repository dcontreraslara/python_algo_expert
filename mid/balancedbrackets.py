def balancedBrackets(string):
    d = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    c = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    if len(string) == 0:
        return True

    if string[0] not in d:
        return False

    s = [string[0]]

    for i in range(1, len(string)):
        if string[i] in d:
            s.append(string[i])
        elif string[i] in c:
            p = s.pop()
            if d[p] != string[i]:
                return False

    return True if len(s) == 0 else False





