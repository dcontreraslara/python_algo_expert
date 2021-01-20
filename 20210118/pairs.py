def maxPairs(skillLevel, minDiff):
    # Write your code here
    skillLevel = sorted(skillLevel)
    print(skillLevel)
    pairs = 0
    j = 0
    i = 1
    visited = set()
    while i < len(skillLevel):
        print(i, j, skillLevel[i] - skillLevel[j])
        if abs(skillLevel[i] - skillLevel[j])>=minDiff and j not in visited:
            visited.add(i)
            pairs=pairs+1
            if j + 1 < i:
                j = j + 1
            else:
                j = i + 1
                i = j
        while j in visited:
            j = j + 1
        if j >=i:
            i = j
        i += 1

    return pairs


# print(maxPairs([306989605, 318554335, 58938146, 376420327, 802573599, 509674780, 939226418, 219080001, 290589043, 345194195],22586934))
# print(maxPairs([3,4,5,2,1,1],3))
#print(maxPairs([58938146, 219080001, 290589043, 306989605, 318554335, 345194195, 376420327, 509674780, 802573599, 939226418], 0))
#print(maxPairs([58938146, 219080001, 290589043, 306989605, 318554335, 345194195, 376420327, 509674780, 802573599, 939226418], 22586934))
print(maxPairs([25107191, 123232501, 151290765, 183012194, 473251358, 579542802, 689345248, 709552565, 803612259, 862726097, 994391793], 440987423))


