def equilateral(sides):
    if sides[0] + sides[1] >= sides[2]:
        if sides[1] + sides[2] >= sides[0]:
            if sides[0] + sides[2] >= sides[1]:
                if not sides[0] == 0:
                    s = set(sides)
                    if len(s) == 1:
                        return True
    return False


def isosceles(sides):
    if sides[0] + sides[1] >= sides[2]:
        if sides[1] + sides[2] >= sides[0]:
            if sides[0] + sides[2] >= sides[1]:
                s = set(sides)
                if len(s) == 2:
                    return True
                elif len(s) == 1:
                    return True
    return False



def scalene(sides):
    if sides[0] + sides[1] >= sides[2]:
        if sides[1] + sides[2] >= sides[0]:
            if sides[0] + sides[2] >= sides[1]:
                s = set(sides)
                if len(s) == 3:
                    return True
    return False



# print(equilateral([2, 2, 2]))
print(isosceles([1, 3, 1]))