import string
import random
from copy import deepcopy

f = open("C:/Users/Tadhg/Documents/Day18.txt", "r+")
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
for j in range(ycount):
    column=[];
    for i in range(xcount):
        column.append(" ");
    grid.append(column);

count=0
for i in range(ycount):
    for j in range(xcount):
        grid[j][i] = cont[count]
        count+=1

keys = string.ascii_lowercase
doors = string.ascii_uppercase
unimportantdoors = ""
endkeys = ""

check = True
while check:
    check = False
    for i in range(ycount):
        for j in range(xcount):
            
            if grid[j][i] == "@":
                startx = j
                starty = i
            
            wallcount=0
            if grid[j][i] == "." or grid[j][i] in doors:
                if grid[j+1][i] == "#":
                    wallcount+=1
                if grid[j-1][i] == "#":
                    wallcount+=1
                if grid[j][i+1] == "#":
                    wallcount+=1
                if grid[j][i-1] == "#":
                    wallcount+=1

                if wallcount == 3:
                    if grid[j][i] in doors:
                        unimportantdoors += grid[j][i]
                    check = True
                    grid[j][i] = "#"
                    
            if grid[j][i] in keys:
                if grid[j+1][i] == "#":
                    wallcount+=1
                if grid[j-1][i] == "#":
                    wallcount+=1
                if grid[j][i+1] == "#":
                    wallcount+=1
                if grid[j][i-1] == "#":
                    wallcount+=1

                if wallcount == 3:
                    if grid[j][i] not in endkeys:
                        endkeys += grid[j][i]

grid2 = deepcopy(grid)

"""for i in range(ycount):
    for j in range(xcount):
        print(grid[j][i], end = '')
    print()"""


class key:
    def __init__(self, name, distance, quadrant):
        self.name = name
        self.distance = distance
        self.quadrant = quadrant

classedkeys = []
turningpointname = 0
paths = []
for i in range(ycount):
    for j in range(xcount):
        if grid[j][i] in endkeys:
            posx = j
            posy = i
            enddistance = 1
            thispath = ""
            loopcount = 0
            classedkeysthispath = []
            while posx != startx and posy != starty:

                loopcount+=1

                if grid[posx][posy] in keys or grid[posx][posy] in doors:
                        thispath += grid[posx][posy]
                        if grid[posx][posy] in keys:
                            if posx>startx and posy>starty:
                                quadrant = 2
                            if posx<startx and posy<starty:
                                quadrant = 3
                            if posx<startx and posy>starty:
                                quadrant = 1
                            if posx>startx and posy<starty:
                                quadrant = 4
                            
                            classedkeysthispath.append(key(grid[posx][posy], enddistance, quadrant))

                grid[posx][posy] = "*"
                enddistance+=1

                viablepaths = 0
                if grid[posx][posy-1] != "#" and grid[posx][posy-1] != "*":
                    viablepaths += 1
                if grid[posx+1][posy] != "#" and grid[posx+1][posy] != "*":
                    viablepaths += 1
                if grid[posx][posy+1] != "#" and grid[posx][posy+1] != "*":
                    viablepaths += 1
                if grid[posx-1][posy] != "#" and grid[posx-1][posy] != "*":
                    viablepaths += 1


                if viablepaths == 1:
                        
                    if grid[posx][posy-1] != "#" and grid[posx][posy-1] != "*":
                        posy-=1                            
                    elif grid[posx+1][posy] != "#" and grid[posx+1][posy] != "*":
                        posx+=1
                    elif grid[posx][posy+1] != "#" and grid[posx][posy+1] != "*":
                        posy+=1
                    elif grid[posx-1][posy] != "#" and grid[posx-1][posy] != "*":
                        posx-=1
                        
                elif viablepaths>1:
                    if posx>startx and posy>starty:
                        quadrant = 2
                    if posx<startx and posy<starty:
                        quadrant = 3
                    if posx<startx and posy>starty:
                        quadrant = 1
                    if posx>startx and posy<starty:
                        quadrant = 4
                    thispath += str(quadrant)
                    
                    turningarray = []
                    if grid[posx][posy-1] != "#" and grid[posx][posy-1] != "*":
                        turningarray.append("up")                            
                    if grid[posx+1][posy] != "#" and grid[posx+1][posy] != "*":
                        turningarray.append("right")
                    if grid[posx][posy+1] != "#" and grid[posx][posy+1] != "*":
                        turningarray.append("down")
                    if grid[posx-1][posy] != "#" and grid[posx-1][posy] != "*":
                        turningarray.append("left")
    
                    randomdirection = str(random.sample(turningarray,1)).replace("['", "").replace("']", "")
                    if randomdirection == "up":
                        posy-=1                            
                    elif randomdirection == "right":
                        posx+=1
                    elif randomdirection == "down":
                        posy+=1
                    elif randomdirection == "left":
                        posx-=1
                                        
                if grid[posx][posy] in endkeys or loopcount == 10000:
                    posx = j
                    posy = i
                    enddistance = 1
                    thispath = ""
                    grid = deepcopy(grid2)
                    loopcount = 0
                    turningpointname = 0

            thispath = thispath[:(len(thispath)-1)]
            paths.append(thispath)
            for r in classedkeysthispath:
                r.distance = enddistance + 1 - r.distance
                classedkeys.append(r)

for i in classedkeys:
    for j in classedkeys:
        if i.name == j.name:
            i.distance = max(i.distance, j.distance)
seenkeys = set()
newclassedkeys = []
for i in classedkeys:
    if i.name + str(i.distance) not in seenkeys:
        if i.name not in keys:
            if str(i.distance) + str(i.quadrant) not in seenkeys:
                newclassedkeys.append(i)
                seenkeys.add(str(i.distance) + str(i.quadrant))
        else:
            newclassedkeys.append(i)
            seenkeys.add(i.name + str(i.distance))

classedkeys = newclassedkeys
"""for i in classedkeys:
    if i.name =="g":
        print("g" + str(i.distance))
    if i.name =="r":
        print("r" + str(i.distance))"""
        

finalpath = "uogw"
additions = 20+4+8+16+160+176
finaldistance = additions
for i in finalpath:
    for j in classedkeys:
        if j.name == i:
            finaldistance += j.distance
finaldistance-=8
print(finaldistance)
"""posx = startx
posy = starty
finalpath = ""
check = False
while check ==False:
    
    viablekeys = []
    blockingdoors = ""
    for i in paths:
        for j in i[::-1]:
            if j in doors:
                blockingdoors += j
                break
            for k in classedkeys:
                if j == k.name:
                    viablekeys.append(k)
                    
    seenviablekeys = set()
    newviablekeys = []
    for i in viablekeys:
        if i.name not in seenviablekeys:
            newviablekeys.append(i)
            seenviablekeys.add(i.name)
    viablekeys = newviablekeys

    blockingdoors = "".join(set(blockingdoors))

    importantkeys = []
    for i in viablekeys:
        if i.name.upper() in blockingdoors:
            importantkeys.append(i)
    for i in importantkeys:
        finalpath += i.name
        paths = [p.replace(i.name.upper(), '') for p in paths]
    if importantkeys == []:
        for i in paths:
            print(finalpath)

    for i in keys:
        if i not in finalpath:
            check = False

print(finalpath)"""
