def runLengthEncoding(string):
    count = 0
    current = string[0]
    out = ""
    for c in string:

        if current == c:
            count += 1
            if count == 10:
                out = out + "9" + current
                count = 1
        else:
            out = out + str(count) + current
            current = c
            count = 1
    out = out + str(count) + current
    return out
