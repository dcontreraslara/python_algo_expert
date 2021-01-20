def circle(commands):
    posx , posy = 0,0
    direction = 1
    c = "".join(commands)
    visited = set()
    for j in range(4):
        visited.add((posx, posy))
        res = []
        found = False
        for i in range(len(c)):
            print(posx,posy, c[i])
            curr = c[i]
            if curr == "R":
                direction = (direction+1)%4
                res.append("NO")
            elif curr == "L":
                direction = (direction+3)%4
                res.append("NO")
            else:
                if direction == 1:
                    posy +=1
                elif direction == 2:
                    posx +=1
                elif direction == 3:
                    posy-=1
                else:
                    posx-=1

        if (posx, posy) in visited:
            res.append("YES")
            return res

    return ["NO"]

#print(circle(["LG"]))
print(circle(["GGGGRRGL"]))






