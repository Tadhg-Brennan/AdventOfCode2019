import string
import random
from copy import deepcopy

f = open("C:/Users/Tadhg/Documents/Day20.txt", "r+")
cont = f.read()
f.close()

xcount = -1
for i in cont:
    xcount+=1
    if i == '\n':
        break
cont = cont.replace('\n', '')    
ycount=0 
for i in cont:
    ycount+=1
    
ycount = int(ycount/xcount)

grid = []
for j in range(xcount):
    column=[];
    for i in range(ycount):
        column.append(" ");
    grid.append(column);

count=0
for i in range(ycount):
    for j in range(xcount):
        grid[j][i] = cont[count]
        count+=1

check = True
while check:
    check = False
    for i in range(ycount):
        for j in range(xcount):
            
            wallcount=0
            if grid[j][i] == ".":
                if grid[j+1][i] == "#":
                    wallcount+=1
                if grid[j-1][i] == "#":
                    wallcount+=1
                if grid[j][i+1] == "#":
                    wallcount+=1
                if grid[j][i-1] == "#":
                    wallcount+=1

                if wallcount == 3:
                    check = True
                    grid[j][i] = "#"
"""
for i in range(ycount):
    for j in range(xcount):
        print(grid[j][i], end = '')
    print()"""
    
class path:
    def __init__(self, outer, inner, distance):
        self.outer = outer
        self.inner = inner
        self.distance = distance

turned = False
paths = []
for i in range(xcount):
    if grid[i][2] == ".":
        outer = grid[i][0] + grid[i][1]
        posx = i
        posy = 2
        enddistance = 0
        turncount = 0

        check = False
        while check == False:

            grid[posx][posy] = "*"
            enddistance+=1

            viablepaths = 0
            if grid[posx][posy-1] == ".":
                viablepaths += 1
            if grid[posx+1][posy] == ".":
                viablepaths += 1
            if grid[posx][posy+1] == ".":
                viablepaths += 1
            if grid[posx-1][posy] == ".":
                viablepaths += 1

            if viablepaths == 0:
                if posy != 2:
                    inner = grid[posx][posy+1]+grid[posx][posy+2]
                    paths.append(path(outer, inner, enddistance))
                else:
                    outer += grid[posx][posy-2]+grid[posx][posy-1]
                    paths.append(path(outer, "", enddistance))
                if turncount == 0:
                    check = True
                else:
                    if turncount>1:
                        enddistance = turningdistance2
                        posx = turningx2
                        posy = turningy2
                    else:
                        enddistance = turningdistance
                        posx = turningx
                        posy = turningy
                    outer = grid[i][0] + grid[i][1]
                    turncount-=1

            elif viablepaths == 1:
                if grid[posx][posy-1] == ".":
                    posy-=1                            
                elif grid[posx+1][posy] == ".":
                    posx+=1
                elif grid[posx][posy+1] == ".":
                    posy+=1
                elif grid[posx-1][posy] == ".":
                    posx-=1

            elif viablepaths>1:
                if turncount == 0:
                    turningx = posx
                    turningy = posy
                    turningdistance = enddistance-1
                if turncount > 0:
                    turningx2 = posx
                    turningy2 = posy
                    turningdistance2 = enddistance-1
                turncount+=1
                posy+=1
        if turned:
            for m in range(ycount):
                for n in range(xcount):
                    if grid[n][m] == "*":
                        grid[n][m] = "."
            turned = False
                
for i in range(ycount):
    if grid[2][i] == ".":
        outer = grid[0][i] + grid[1][i]
        posx = 2
        posy = i
        enddistance = 0
        turncount = 0

        check = False
        while check == False:

            grid[posx][posy] = "*"
            enddistance+=1

            viablepaths = 0
            if grid[posx][posy-1] == ".":
                viablepaths += 1
            if grid[posx+1][posy] == ".":
                viablepaths += 1
            if grid[posx][posy+1] == ".":
                viablepaths += 1
            if grid[posx-1][posy] == ".":
                viablepaths += 1

            if viablepaths == 0:
                if posx != 2:
                    inner = grid[posx+1][posy]+grid[posx+2][posy]
                    paths.append(path(outer, inner, enddistance))
                else:
                    outer += grid[posx-2][posy]+grid[posx-1][posy]
                    paths.append(path(outer, "", enddistance))
                if turncount == 0:
                    check = True
                else:
                    if turncount>1:
                        enddistance = turningdistance2-1
                        posx = turningx2
                        posy = turningy2
                    else:
                        enddistance = turningdistance-1
                        posx = turningx
                        posy = turningy
                    outer = grid[0][i] + grid[1][i]
                    turncount-=1

            elif viablepaths == 1:
                if grid[posx][posy-1] == ".":
                    posy-=1                            
                elif grid[posx+1][posy] == ".":
                    posx+=1
                elif grid[posx][posy+1] == ".":
                    posy+=1
                elif grid[posx-1][posy] == ".":
                    posx-=1

            elif viablepaths>1:
                if turncount == 0:
                    turningx = posx
                    turningy = posy
                    turningdistance = enddistance-1
                if turncount > 0:
                    turningx2 = posx
                    turningy2 = posy
                    turningdistance2 = enddistance-1
                turncount+=1
                turned = True
                posx+=1
        if turned:
            for m in range(ycount):
                for n in range(xcount):
                    if grid[n][m] == "*":
                        grid[n][m] = "."
            turned = False
                         
for i in range(xcount):
    if grid[i][ycount-3] == ".":
        outer = grid[i][ycount-2] + grid[i][ycount-1]
        posx = i
        posy = ycount-3
        enddistance = 0
        turncount = 0

        check = False
        while check == False:

            grid[posx][posy] = "*"
            enddistance+=1

            viablepaths = 0
            if grid[posx][posy-1] == ".":
                viablepaths += 1
            if grid[posx+1][posy] == ".":
                viablepaths += 1
            if grid[posx][posy+1] == ".":
                viablepaths += 1
            if grid[posx-1][posy] == ".":
                viablepaths += 1

            if viablepaths == 0:
                if posy != ycount-3:
                    inner = grid[posx][posy-2]+grid[posx][posy-1]
                    paths.append(path(outer, inner, enddistance))
                else:
                    outer += grid[posx][posy+1]+grid[posx][posy+2]
                    paths.append(path(outer, "", enddistance))
                if turncount == 0:
                    check = True
                else:
                    if turncount>1:
                        enddistance = turningdistance2-1
                        posx = turningx2
                        posy = turningy2
                    else:
                        enddistance = turningdistance-1
                        posx = turningx
                        posy = turningy
                    outer = grid[i][ycount-2] + grid[i][ycount-1]
                    turncount-=1

            elif viablepaths == 1:
                if grid[posx][posy-1] == ".":
                    posy-=1                            
                elif grid[posx+1][posy] == ".":
                    posx+=1
                elif grid[posx][posy+1] == ".":
                    posy+=1
                elif grid[posx-1][posy] == ".":
                    posx-=1

            elif viablepaths>1:
                if turncount == 0:
                    turningx = posx
                    turningy = posy
                    turningdistance = enddistance
                if turncount > 0:
                    turningx2 = posx
                    turningy2 = posy
                    turningdistance2 = enddistance
                turncount+=1
                turned = True
                posx-=1
        if turned:
            for m in range(ycount):
                for n in range(xcount):
                    if grid[n][m] == "*":
                        grid[n][m] = "."
            turned = False
                
for i in range(ycount):
    if grid[xcount-3][i] == ".":
        outer = grid[xcount-2][i] + grid[xcount-1][i]
        posx = xcount-3
        posy = i
        enddistance = 0
        turncount = 0

        check = False
        while check == False:

            grid[posx][posy] = "*"
            enddistance+=1

            viablepaths = 0
            if grid[posx][posy-1] == ".":
                viablepaths += 1
            if grid[posx+1][posy] == ".":
                viablepaths += 1
            if grid[posx][posy+1] == ".":
                viablepaths += 1
            if grid[posx-1][posy] == ".":
                viablepaths += 1

            if viablepaths == 0:
                if posx != xcount-3:
                    inner = grid[posx-2][posy]+grid[posx-1][posy]
                    paths.append(path(outer, inner, enddistance))
                else:
                    outer += grid[posx+1][posy]+grid[posx+2][posy]
                    paths.append(path(outer, "", enddistance))
                if turncount == 0:
                    check = True
                else:
                    if turncount>1:
                        enddistance = turningdistance2
                        posx = turningx2
                        posy = turningy2
                    else:
                        enddistance = turningdistance
                        posx = turningx
                        posy = turningy
                    outer = grid[xcount-2][i] + grid[xcount-1][i]
                    turncount-=1

            elif viablepaths == 1:
                if grid[posx][posy-1] == ".":
                    posy-=1                            
                elif grid[posx+1][posy] == ".":
                    posx+=1
                elif grid[posx][posy+1] == ".":
                    posy+=1
                elif grid[posx-1][posy] == ".":
                    posx-=1

            elif viablepaths>1:
                if turncount == 0:
                    turningx = posx
                    turningy = posy
                    turningdistance = enddistance
                if turncount > 0:
                    turningx2 = posx
                    turningy2 = posy
                    turningdistance2 = enddistance
                turncount+=1
                turned = True
                posx-=1
        if turned:
            for m in range(ycount):
                for n in range(xcount):
                    if grid[n][m] == "*":
                        grid[n][m] = "."
            turned = False
                          

for i in paths:
    print(i.outer, i.inner, i.distance)

class option:
    def __init__(self, name, outertoinner, distance):
        self.name = name
        self.outertoinner = outertoinner
        self.distance = distance

def nextdoor(currentcheck, outertoinner, visited):
    options = []
    for i in paths:
        if outertoinner:
            if i.outer[0] + i.outer[1] == currentcheck:
                if i.inner == "":
                    outertoinner = False
                    if i.outer[2]+i.outer[3] == "ZZ":
                        options = []
                        options.append(option(i.outer[2]+i.outer[3], outertoinner, i.distance))
                        return options
                    elif i.outer[2]+i.outer[3] not in visited:
                        options.append(option(i.outer[2]+i.outer[3], outertoinner, i.distance))
                else:
                    if i.inner not in visited:
                        options.append(option(i.inner, outertoinner, i.distance))
        else:
            if i.inner != "":
                if i.inner[0] + i.inner[1] == currentcheck:
                    if i.outer == "ZZ":
                        options = []
                        options.append(option(i.outer, outertoinner, i.distance))
                        return options
                    elif i.outer == "":
                        outertoinner = True
                        if i.inner[2]+i.inner[3] not in visited:
                            options.append(option(i.inner[2]+i.inner[3], outertoinner, i.distance))
                    else:
                        if i.outer not in visited:
                            options.append(option(i.outer, outertoinner, i.distance))
    return options

def finalloop(currentcheck, outertoinner, visited, finaldistance):
    finishedpath = False
    while finishedpath == False:
        print(visited)
        options = nextdoor(currentcheck, outertoinner, visited)
        optionscount = 0
        for i in options:
            optionscount+=1
        if optionscount == 1:
            if options[0].name in visited:
                finishedpath = True
            else:
                currentcheck = options[0].name
                finaldistance += options[0].distance
                visited += currentcheck
                if currentcheck == "ZZ":
                    finishedpath = True
        if optionscount>1:
            for i in options:
                enteredcount = 0
                if i.name not in visited:
                    finalloop(i.name, i.outertoinner, visited+i.name, finaldistance + i.distance)
                    enteredcount +=1
                if enteredcount == 0:
                    finishedpath = True
    return finaldistance

outertoinner = True
currentcheck = "AA"
finaldistance = 0
visited = "AA"
print(finalloop(currentcheck, outertoinner, visited, finaldistance))
