import sys
f=open(sys.argv[1],'r')
commands = []
for line in f.readlines():
   commands.append(line.split()) 
f.close()
board = [["R1","N1","B1","QU","KI","B2","N2","R2"],["P1","P2","P3","P4","P5","P6","P7","P8"],["  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  "],["p1","p2","p3","p4","p5","p6","p7","p8"],["r1","n1","b1","qu","ki","b2","n2","r2"]]
white = ["p1","p2","p3","p4","p5","p6","p7","p8","r1","n1","b1","qu","b2","n2","r2"]
black = ["R1","N1","B1","QU","B2","N2","R2","P1","P2","P3","P4","P5","P6","P7","P8"]
def findinghorizantal(k):
    for i in range(len(board)):
        lists = board[i]
        x = 0 
        if lists.count(k) == 1:
            z = lists.index(k)
            x = x + z
            break
    return int(x)
def findingvertical(k):
    for i in range(len(board)):
        lists = board[i] 
        y = 0
        if lists.count(k) == 1:
            y = y + i
            break
    return int(y)
def listToCoordinate(x):
    result = ''
    if x == 0:
        result = "a"
    elif x == 1:
        result = "b"
    elif x == 2:
        result = "c"
    elif x == 3:
        result = "d"
    elif x == 4:
        result = "e"
    elif x == 5:
        result = "f"
    elif x == 6:
        result = "g"
    elif x == 7:
        result = "h"
    return result
def coordinateToList(k):
    result = 0
    if k == "a":
        result += 0
    elif k == "b":
        result += 1
    elif k == "c":
        result += 2
    elif k == "d":
        result += 3
    elif k == "e":
        result += 4
    elif k == "f":
        result += 5
    elif k == "g":
        result += 6
    elif k == "h":
        result += 7
    return int(result)
def pieceCol(t):
    result = 0 
    if  t[:1].isupper() == False:
        result = -1
    else:
        result = 1
    return result
def reverseCol(t):
    colour = []
    if pieceCol(t) == 1:
        colour = white
    else:
        colour = black
    return colour
def showmovesPawn(b):
    List = reverseCol(b)
    k = pieceCol(b)
    x = findinghorizantal(b)
    y = findingvertical(b)
    possiblemoves = []
    if y < 7 and y > -1:
        if board[y+k][x] == "  " or board[y+k][x] in List:
            List = []
            List.append(listToCoordinate(x))
            List.append(str(8-(y+k)))
            possiblemoves.append("".join(List))
        if len(possiblemoves) == 0:
            return list("FAILED")
    else:
        return list("FAILED")
    return possiblemoves
def showmovesKnight(b):    
    knightcol = reverseCol(b)
    possiblemoves1 = []
    x = findinghorizantal(b)
    y = findingvertical(b)
    if y < 7 and y > 0:
        if x < 7 and x > 0:
            for j in [-1,1]:
                if board[y+j][x+j] == "  ":
                    List = []
                    List.append(listToCoordinate(x+j))
                    List.append(str(8-(y+j)))
                    possiblemoves1.append("".join(List))
                if board[y-j][x+j] == "  ":
                    List = []
                    List.append(listToCoordinate(x+j))
                    List.append(str(8-(y-j)))
                    possiblemoves1.append("".join(List))
        elif x == 7:
            for j in [-1,1]:
                if board[y+j][x-1] == "  " :
                    List1 = []
                    List1.append(listToCoordinate(x-1))
                    List1.append(str(8-(y+j)))
                    possiblemoves1.append("".join(List1))
                if board[y+j][x-1] == "  " :
                    List1 = []
                    List1.append(listToCoordinate(x-1))
                    List1.append(str(8-(y+j)))
                    possiblemoves1.append("".join(List1))
        elif x == 0:
            for j in [-1,1]:
                if board[y+j][x+1] == "  " :
                    List1 = []
                    List1.append(listToCoordinate(x+1))
                    List1.append(str(8-(y+j)))
                    possiblemoves1.append("".join(List1))
                if board[y+j][x+1] == "  " :
                    List1 = []
                    List1.append(listToCoordinate(x+1))
                    List1.append(str(8-(y+j)))
                    possiblemoves1.append("".join(List1))
    if y == 7 and x != 0  and x != 7:
        if board[y-1][x-1] == "  ":
            List = []
            List.append(listToCoordinate(x-1))
            List.append(str(8-(y-1)))
            possiblemoves1.append("".join(List))
        if board[y-1][x+1] == "  ":
            List = []
            List.append(listToCoordinate(x+1))
            List.append(str(8-(y-1)))
            possiblemoves1.append("".join(List))
    if y == 0 and x != 0  and x != 7:
        if board[y+1][x+1] == "  ":
                List = []
                List.append(listToCoordinate(x+1))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
        if board[y+1][x-1] == "  ":
                List = []
                List.append(listToCoordinate(x-1))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))   
    if y < 6 and y > 1:
        if x != 0 and x != 7:
            for j in [-1,1]:
                if board[y+2*j][x+j] == "  " or board[y+2*j][x+j] in knightcol:
                    List = []
                    List.append(listToCoordinate(x+j))
                    List.append(str(8-(y+2*j)))
                    possiblemoves1.append("".join(List))
                if board[y+2*j][x-j] == "  " or board[y+2*j][x-j] in knightcol:
                    List = []
                    List.append(listToCoordinate(x-j))
                    List.append(str(8-(y+2*j)))
                    possiblemoves1.append("".join(List))
        if x == 0:
            if board[y+2][x+1] == "  " or board[y+2][x+1] in knightcol:
                List = []
                List.append(listToCoordinate(x+1))
                List.append(str(8-(y+2)))
                possiblemoves1.append("".join(List))
            if board[y-2][x+1] == "  " or board[y-2][x+1] in knightcol:
                List = []
                List.append(listToCoordinate(x+1))
                List.append(str(8-(y-2)))
                possiblemoves1.append("".join(List))
        if x == 7 :
            if board[y-2][x-1] == "  " or board[y-2][x-1] in knightcol:
                List = []
                List.append(listToCoordinate(x-1))
                List.append(str(8-(y-2)))
                possiblemoves1.append("".join(List))
            if board[y+2][x-1] == "  " or board[y+2][x-1] in knightcol:
                List = []
                List.append(listToCoordinate(x-1))
                List.append(str(8-(y+2)))
                possiblemoves1.append("".join(List))
    if y == 0 or y == 1:
        if x > 0 and x < 7 :
            if board[y+2][x+1] == "  " or board[y+2][x+1] in knightcol:
                List = []
                List.append(listToCoordinate(x+1))
                List.append(str(8-(y+2)))
                possiblemoves1.append("".join(List))
            if board[y+2][x-1] == "  " or board[y+2][x-1] in knightcol:
                List = []
                List.append(listToCoordinate(x-1))
                List.append(str(8-(y+2)))
                possiblemoves1.append("".join(List))
        if x == 0:# (0,0) ın hareketleri
            if board[y+2][x+1] == "  " or board[y+2][x+1] in knightcol:
                List = []
                List.append(listToCoordinate(x+1))
                List.append(str(8-(y+2)))
                possiblemoves1.append("".join(List))
            if board[y+1][x+1] == "  ":
                List = []
                List.append(listToCoordinate(x+1))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
            if board[y+1][x+2] == "  " or board[y+1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
        if x == 7:# (0,7) nin hareketleri
            if board[y+2][x-1] == "  " or board[y+2][x-1] in knightcol:
                List = []
                List.append(listToCoordinate(x-1))
                List.append(str(8-(y+2)))
                possiblemoves1.append("".join(List))
            if board[y+1][x-1] == "  ":
                List = []
                List.append(listToCoordinate(x-1))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
            if board[y+1][x-2] == "  " or board[y+1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
    if y == 7 or y == 6:
        if x > 0 and x < 7 :
            if board[y-2][x+1] == "  " or board[y-2][x+1] in knightcol:
                List = []
                List.append(listToCoordinate(x+1))
                List.append(str(8-(y-2)))
                possiblemoves1.append("".join(List))
            if board[y-2][x-1] == "  " or board[y-2][x-1] in knightcol:
                List = []
                List.append(listToCoordinate(x-1))
                List.append(str(8-(y-2)))
                possiblemoves1.append("".join(List))
        if x == 0:
            if board[y-2][x+1] == "  " or board[y-2][x+1] in knightcol:
                List = []
                List.append(listToCoordinate(x+1))
                List.append(str(8-(y-2)))
                possiblemoves1.append("".join(List))
            if board[y-1][x+1] == "  ":
                List = []
                List.append(listToCoordinate(x+1))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
            if board[y-1][x+2] == "  " or board[y+1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
        if x == 7:
            if board[y-2][x-1] == "  " or board[y+2][x-1] in knightcol:
                List = []
                List.append(listToCoordinate(x-1))
                List.append(str(8-(y-2)))
                possiblemoves1.append("".join(List))
            if board[y-1][x-1] == "  ":
                List = []
                List.append(listToCoordinate(x-1))
                List.append(str(8-(-+1)))
                possiblemoves1.append("".join(List))
            if board[y-1][x-2] == "  " or board[y+1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
    if x < 6 and x > 1:
        if y != 0 and y != 7:
            if board[y+1][x+2] == "  " or board[y+1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
            if board[y+1][x-2] == "  " or board[y+1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
            if board[y-1][x+2] == "  " or board[y-1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
            if board[y-1][x-2] == "  " or board[y-1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
        if y == 0:
            if board[y+1][x+2] == "  " or board[y+1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
            if board[y+1][x-2] == "  " or board[y+1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
        if y == 7:
            if board[y-1][x+2] == "  " or board[y-1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
            if board[y-1][x-2] == "  " or board[y-1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
    if x == 6 or x == 7:
        if y < 7 and y > 1:
            if board[y+1][x-2] == "  " or board[y+1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
            if board[y-1][x-2] == "  " or board[y-1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
        if y == 7:
            if board[y-1][x-2] == "  " or board[y-1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
        if y == 0:
            if board[y+1][x-2] == "  " or board[y+1][x-2] in knightcol:
                List = []
                List.append(listToCoordinate(x-2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
    if x == 1 or x == 0:
        if y < 7 and y > 1:
            if board[y+1][x+2] == "  " or board[y+1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
            if board[y-1][x+2] == "  " or board[y-1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
        if y == 7:
            if board[y-1][x+2] == "  " or board[y-1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y-1)))
                possiblemoves1.append("".join(List))
        if y == 0:
            if board[y+1][x+2] == "  " or board[y+1][x+2] in knightcol:
                List = []
                List.append(listToCoordinate(x+2))
                List.append(str(8-(y+1)))
                possiblemoves1.append("".join(List))
    possiblemoves1 = sorted(set(possiblemoves1))
    if len(possiblemoves1) == 0:
        return list("FAILED")
    return possiblemoves1
def showmovesBishop(b):
    k = pieceCol(b)
    List = reverseCol(b)    
    x = findinghorizantal(b)
    y = findingvertical(b)
    possiblemoves = []
    for j in range(1,8):
        if x + j < 8:
            if y+j*k > -1:
                if board[y+j*k][x+j] == "  " or board[y+j*k][x+j] in List:
                    List1 = []
                    List1.append(listToCoordinate(x+j))
                    List1.append(str(8-(y+j*k)))
                    possiblemoves.append("".join(List1))
                    if board[y+j*k][x+j] in List:
                        break
                else:
                    break
            else:
                break
        else:
            break
    for j in range(1,8):
        if x - j >-1:
            if y+j*k > -1:
                if board[y+j*k][x-j] == "  " or board[y+j*k][x-j] in List:
                    List1 = []
                    List1.append(listToCoordinate(x-j))
                    List1.append(str(8-(y+j*k)))
                    possiblemoves.append("".join(List1))
                    if board[y+j*k][x-j] in List:
                        break
                else:
                    break
            else:
                break
        else:
            break
    if len(possiblemoves) == 0:
        return list("FAILED")
    possiblemoves = sorted(set(possiblemoves))
    return possiblemoves
def showmovesRook(b):
    List = reverseCol(b)    
    x = findinghorizantal(b)
    y = findingvertical(b)
    possiblemoves = []
    for j in range(1,8) :
        if x + j < 8:
            if board[y][x+j] == "  " or board[y][x+j] in List:
                List1 = []
                List1.append(listToCoordinate(x+j))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
                if board[y][x+j] in List:
                    break
            else:
                break
    for j in range(1,8) :
        if x - j > -1 :
            if board[y][x-j] == "  " or board[y][x-j] in List:
                List1 = []
                List1.append(listToCoordinate(x-j))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
                if board[y][x-j] in List:
                    break
            else:
                break
        else:
            break
    for j in range(1,8) :
        if y + j < 8:
            if board[y+j][x] == "  " or board[y+j][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y+j)))
                possiblemoves.append("".join(List1))
                if board[y+j][x] in List:
                    break
            else:
                break
    for j in range(1,8) :
        if y - j > -1 :
            if board[y-j][x] == "  " or board[y-j][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y-j)))
                possiblemoves.append("".join(List1))
                if board[y-j][x] in List:
                    break
            else:
                break
        else:
            break
    if len(possiblemoves) == 0:
        return list("FAILED")
    possiblemoves = sorted(set(possiblemoves))
    return possiblemoves
def showmovesQueen(b):
    List = reverseCol(b)    
    x = findinghorizantal(b)
    y = findingvertical(b)
    possiblemoves = []
    for j in range(1,8) :
        if x + j < 8:
            if board[y][x+j] == "  " or board[y][x+j] in List:
                List1 = []
                List1.append(listToCoordinate(x+j))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
                if board[y][x+j] in List:
                    break
            else:
                break
    for j in range(1,8) :
        if x - j > -1 :
            if board[y][x-j] == "  " or board[y][x-j] in List:
                List1 = []
                List1.append(listToCoordinate(x-j))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
                if board[y][x-j] in List:
                    break
            else:
                break
        else:
            break
    for j in range(1,8) :
        if y + j < 8:
            if board[y+j][x] == "  " or board[y+j][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y+j)))
                possiblemoves.append("".join(List1))
                if board[y+j][x] in List:
                    break
            else:
                break
    for j in range(1,8) :
        if y - j > -1 :
            if board[y-j][x] == "  " or board[y-j][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y-j)))
                possiblemoves.append("".join(List1))
                if board[y-j][x] in List:
                    break
            else:
                break
        else:
            break
    for j in range(1,8):
        if x + j < 8:
            if y+j < 8:
                if board[y+j][x+j] == "  " or board[y+j][x+j] in List:
                    List1 = []
                    List1.append(listToCoordinate(x+j))
                    List1.append(str(8-(y+j)))
                    possiblemoves.append("".join(List1))
                    if board[y+j][x+j] in List:
                        break
                else:
                    break
            else:
                break
        else:
            break
    for j in range(1,8):
        if x - j >-1:
            if y+j < 8:
                if board[y+j][x-j] == "  " or board[y+j][x-j] in List:
                    List1 = []
                    List1.append(listToCoordinate(x-j))
                    List1.append(str(8-(y+j)))
                    possiblemoves.append("".join(List1))
                    if board[y+j][x-j] in List:
                        break
                else:
                    break
            else:
                break
        else:
            break
    for j in range(1,8):
        if x + j < 8:
            if y-j > -1:
                if board[y-j][x+j] == "  " or board[y-j][x+j] in List:
                    List1 = []
                    List1.append(listToCoordinate(x+j))
                    List1.append(str(8-(y-j)))
                    possiblemoves.append("".join(List1))
                    if board[y-j][x+j] in List:
                        break
                else:
                    break
            else:
                break
        else:
            break
    for j in range(1,8):
        if x - j >-1:
            if y-j > -1:
                if board[y-j][x-j] == "  " or board[y-j][x-j] in List:
                    List1 = []
                    List1.append(listToCoordinate(x-j))
                    List1.append(str(8-(y-j)))
                    possiblemoves.append("".join(List1))
                    if board[y-j][x-j] in List:
                        break
                else:
                    break
            else:
                break
        else:
            break
    if len(possiblemoves) == 0:
        return list("FAILED")
    possiblemoves = sorted(set(possiblemoves))
    return possiblemoves
def showmovesKing(b):
    List = reverseCol(b)
    possiblemoves = []
    x = findinghorizantal(b)
    y = findingvertical(b)
    if y < 7 and y > 0:
        if x < 7 and x > 0:
            for j in [-1,1]:
                if board[y][x+j] == "  " or board[y][x+j] in List:
                    List1 = []
                    List1.append(listToCoordinate(x+j))
                    List1.append(str(8-(y)))
                    possiblemoves.append("".join(List1))
                if board[y+j][x] == "  " or board[y+j][x] in List:
                    List1 = []
                    List1.append(listToCoordinate(x))
                    List1.append(str(8-(y+j)))
                    possiblemoves.append("".join(List1))
                if board[y+j][x+j] == "  " or board[y+j][x+j] in List:
                    List1 = []
                    List1.append(listToCoordinate(x+j))
                    List1.append(str(8-(y+j)))
                    possiblemoves.append("".join(List1))
                if board[y+j][x-j] == "  " or board[y+j][x-j] in List:
                    List1 = []
                    List1.append(listToCoordinate(x-j))
                    List1.append(str(8-(y+j)))
                    possiblemoves.append("".join(List1))
        if x == 7:
            for j in [-1,1]:
                if board[y+j][x] == "  " or board[y+j][x] in List:
                    List1 = []
                    List1.append(listToCoordinate(x))
                    List1.append(str(8-(y+j)))
                    possiblemoves.append("".join(List1))
                if board[y+j][x-1] == "  " or board[y+j][x-1] in List:
                    List1 = []
                    List1.append(listToCoordinate(x-1))
                    List1.append(str(8-(y+j)))
                    possiblemoves.append("".join(List1))
                if board[y][x-1] == "  " or board[y][x-1] in List:
                    List1 = []
                    List1.append(listToCoordinate(x-1))
                    List1.append(str(8-(y)))
                    possiblemoves.append("".join(List1))
        if x == 0:
            for j in [-1,1]:
                if board[y+j][x] == "  " or board[y+j][x] in List:
                    List1 = []
                    List1.append(listToCoordinate(x))
                    List1.append(str(8-(y+j)))
                    possiblemoves.append("".join(List1))
                if board[y+j][x+1] == "  " or board[y+j][x+1] in List:
                    List1 = []
                    List1.append(listToCoordinate(x+1))
                    List1.append(str(8-(y+j)))
                    possiblemoves.append("".join(List1))
                if board[y][x+1] == "  " or board[y][x+1] in List:
                    List1 = []
                    List1.append(listToCoordinate(x+1))
                    List1.append(str(8-(y)))
                    possiblemoves.append("".join(List1))
    if y == 7:
        if x == 0 :
            if board[y][x+1] == "  " or board[y][x+1] in List:
                List1 = []
                List1.append(listToCoordinate(x+1))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
            if board[y-1][x+1] == "  " or board[y-1][x+1] in List:
                List1 = []
                List1.append(listToCoordinate(x+1))
                List1.append(str(8-(y-1)))
                possiblemoves.append("".join(List1))
            if board[y-1][x] == "  " or board[y-1][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y-1)))
                possiblemoves.append("".join(List1))
        if x == 7 :
            if board[y][x-1] == "  " or board[y][x-1] in List:
                List1 = []
                List1.append(listToCoordinate(x-1))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
            if board[y-1][x-1] == "  " or board[y-1][x-1] in List:
                List1 = []
                List1.append(listToCoordinate(x-1))
                List1.append(str(8-(y-1)))
                possiblemoves.append("".join(List1))
            if board[y-1][x] == "  " or board[y-1][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y-1)))
                possiblemoves.append("".join(List1))
        if x > 0 and x < 7:
            if board[y][x-1] == "  " or board[y][x-1] in List:
                List1 = []
                List1.append(listToCoordinate(x-1))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
            if board[y][x+1] == "  " or board[y][x+1] in List:
                List1 = []
                List1.append(listToCoordinate(x+1))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
            if board[y-1][x-1] == "  " or board[y-1][x-1] in List:
                List1 = []
                List1.append(listToCoordinate(x-1))
                List1.append(str(8-(y-1)))
                possiblemoves.append("".join(List1))
            if board[y-1][x+1] == "  " or board[y-1][x+1] in List:
                List1 = []
                List1.append(listToCoordinate(x+1))
                List1.append(str(8-(y-1)))
                possiblemoves.append("".join(List1))
            if board[y-1][x] == "  " or board[y-1][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y-1)))
                possiblemoves.append("".join(List1))
    if y == 0:
        if x == 0 :
            if board[y][x+1] == "  " or board[y][x+1] in List:
                List1 = []
                List1.append(listToCoordinate(x+1))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
            if board[y+1][x+1] == "  " or board[y-1][x+1] in List:
                List1 = []
                List1.append(listToCoordinate(x+1))
                List1.append(str(8-(y+1)))
                possiblemoves.append("".join(List1))
            if board[y+1][x] == "  " or board[y+1][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y+1)))
                possiblemoves.append("".join(List1))
        if x == 7 :
            if board[y][x-1] == "  " or board[y][x-1] in List:
                List1 = []
                List1.append(listToCoordinate(x-1))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
            if board[y+1][x-1] == "  " or board[y+1][x-1] in List:
                List1 = []
                List1.append(listToCoordinate(x-1))
                List1.append(str(8-(y+1)))
                possiblemoves.append("".join(List1))
            if board[y+1][x] == "  " or board[y+1][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y-1)))
                possiblemoves.append("".join(List1))
        if x != 0 and x != 7:
            if board[y][x+1] == "  " or board[y][x+1] in List:
                List1 = []
                List1.append(listToCoordinate(x+1))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
            if board[y][x-1] == "  " or board[y][x-1] in List:
                List1 = []
                List1.append(listToCoordinate(x-1))
                List1.append(str(8-(y)))
                possiblemoves.append("".join(List1))
            if board[y+1][x+1] == "  " or board[y+1][x+1] in List:
                List1 = []
                List1.append(listToCoordinate(x+1))
                List1.append(str(8-(y+1)))
                possiblemoves.append("".join(List1))
            if board[y+1][x-1] == "  " or board[y+1][x-1] in List:
                List1 = []
                List1.append(listToCoordinate(x-1))
                List1.append(str(8-(y+1)))
                possiblemoves.append("".join(List1))
            if board[y+1][x] == "  " or board[y+1][x] in List:
                List1 = []
                List1.append(listToCoordinate(x))
                List1.append(str(8-(y+1)))
                possiblemoves.append("".join(List1))
    if len(possiblemoves) == 0:
        return list("FAILED")
    possiblemoves = sorted(set(possiblemoves))
    return possiblemoves
def move(q,w):
    showmoves = []
    if q[:1] == 'n' or q[:1] == 'N':
        showmoves.extend(showmovesKnight(q))
    elif q[:1] == 'b' or q[:1] == 'B':
        showmoves.extend(showmovesBishop(q))
    elif q[:1] == 'r' or q[:1] == 'R':
        showmoves.extend(showmovesRook(q))
    elif q[:1] == 'q' or q[:1] == 'Q':
        showmoves.extend(showmovesQueen(q))
    elif q[:1] == 'k' or q[:1] == 'K':
        showmoves.extend(showmovesKing(q))
    elif q[:1] == 'p' or q[:1] == 'P':
        showmoves.extend(showmovesPawn(q))
    x = findinghorizantal(q)
    y = findingvertical(q)
    if showmoves == "FAILED":
        return print(*list("FAILED"))
    elif w in showmoves:
        k = coordinateToList(w[0:1])
        l = 8 - int(w[1:])
        board[y][x] = "  "
        board[l][k] = q
        return print("OK")
    else:
        return print(*list("FAILED"))
for i in range(len(commands)):
    print(">",*commands[i])
    if commands[i][0] == "showmoves":
        if commands[i][1][:1] == 'p' or commands[i][1][:1] == 'P':
            print(*showmovesPawn(commands[i][1]))
        elif commands[i][1][:1] == 'n' or commands[i][1][:1] == 'N':
            print(*showmovesKnight(commands[i][1]))
        elif commands[i][1][:1] == 'b' or commands[i][1][:1] == 'B':
            print(*showmovesBishop(commands[i][1]))
        elif commands[i][1][:1] == 'R' or commands[i][1][:1] == 'r':
            print(*showmovesRook(commands[i][1]))
        elif commands[i][1][:1] == 'q' or commands[i][1][:1] == 'Q':
            print(*showmovesQueen(commands[i][1]))
        elif commands[i][1][:1] == 'k' or commands[i][1][:1] == 'K':
            print(*showmovesKing(commands[i][1])) 
    elif commands[i] == ['print']:
        print("-"*23)
        for i in board:
            print(*i)
        print("-"*23)
    elif commands[i] == ['initialize']:
        board = [["R1","N1","B1","QU","KI","B2","N2","R2"],
            ["P1","P2","P3","P4","P5","P6","P7","P8"],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["p1","p2","p3","p4","p5","p6","p7","p8"],
            ["r1","n1","b1","qu","ki","b2","n2","r2"]] 
        print("OK")
        print("-"*23)
        for i in board:
            print(*i)
        print("-"*23)
        board = [["R1","N1","B1","QU","KI","B2","N2","R2"],
            ["P1","P2","P3","P4","P5","P6","P7","P8"],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["p1","p2","p3","p4","p5","p6","p7","p8"],
            ["r1","n1","b1","qu","ki","b2","n2","r2"]]          
    elif commands[i][0] == 'move': move(commands[i][1],commands[i][2])
    elif commands[i] == ["exit"]: exit()
