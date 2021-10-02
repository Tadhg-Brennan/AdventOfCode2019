f = open("C:/Users/Tadhg/Documents/Day10.txt", "r+");
contents = f.read().splitlines();
f.close()

cont = list(contents)

grid = []
icount = 0
jcount = 0
outputs = []

for i in cont[0]:
    column = []
    for j in cont:
        column.append(0)
    grid.append(column)

for i in cont:
    jcount = 0
    for j in cont[icount]:
        grid[icount][jcount] = j
        jcount += 1
    icount += 1

angle = 0;
icount = 0
for i in cont:
    jcount = 0
    for j in cont[icount]:
        if grid[icount][jcount] == '#':
            asteroidcount = 0
            angles = []
            icount1 = 0
            for i in cont:
                jcount1 = 0
                for j in cont[icount1]:
                    if grid[icount1][jcount1] == '#':
                        if icount == icount1:
                            if jcount < jcount1:
                                angle = "U"
                            if jcount > jcount1:
                                angle = "D"
                        elif jcount == jcount1:
                            if icount < icount1:
                                angle = "L"
                            if icount > icount1:
                                angle = "R"
                        else:
                            angle = str((jcount-jcount1)/(icount-icount1))
                            if jcount>jcount1:
                                angle += "U"
                        if angle not in angles:
                            asteroidcount += 1
                            angles.append(angle)
                    jcount1 += 1
                icount1 += 1
            outputs.append(asteroidcount)
            if asteroidcount == 210:
               print(jcount, icount)
        
        jcount += 1
    icount += 1

print(max(outputs))
