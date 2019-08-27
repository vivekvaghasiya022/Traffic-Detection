def isOutofRange(a, b, c, d):
    if((a < 0 or a > 100) or (b < 0 or b > 100) or (c < 0 or c > 100) or (d < 0 or d > 100)):
        return True
    else:
        return False


def mini(a, b, c):
    if a ==  min(a,b,c):
        return "Exit 1"
    elif b == min(a, b, c):
        return "Exit 2"
    elif c == min(a, b, c):
        return "Exit 3"


def findBestRoute(incoming, exit1, exit2, exit3):
    if(isOutofRange(incoming, exit1, exit2, exit3)):
        return "Invalid Inputs..."
    return [incoming, min(exit1, exit2, exit3), mini(exit1,exit2,exit2)]


print(findBestRoute(22, 20, 15, 55))
