def intcode(cont):
    x = 0;
    answer = []
    relativebase = 0;
    instruction = "00"
    while instruction != "99":
        value = str(cont[x]).zfill(5)
        instruction = value[3:]
        

        if instruction != "99":
            a = cont[x+1]
            if instruction != "03" and instruction != "04" and instruction != "09":
                b = cont[x+2]
                c = cont[x+3]

            if value[2] == "0":
                if len(cont) <= a:
                    while len(cont) <= a:
                        cont.append(0)
                d = cont[a]
            if value[2] == "1":
                d = a
            if value[2] == "2":
                if len(cont) <= relativebase+a:
                    while len(cont) <= relativebase+a:
                        cont.append(0)
                d = cont[relativebase+a]

            if instruction != "03" and instruction != "04" and instruction != "09":
                if value[1] == "0":
                    if len(cont) <= b:
                        while len(cont) <= b:
                            cont.append(0)
                    e = cont[b]
                if value[1] == "1":
                    e = b
                if value[1] == "2":
                    if len(cont) <= relativebase+b:
                        while len(cont) <= relativebase+b:
                            cont.append(0)
                    e = cont[relativebase+b]

        if instruction == "01" or instruction == "02" or instruction == "07" or instruction == "08":
            if value[0] == "2":
                if len(cont) <= relativebase+c:
                    while len(cont) <= relativebase+c:
                        cont.append(0)
            elif len(cont) <= c:
                while len(cont) <= c:
                    cont.append(0)

        if instruction == "01":
            if value[0] == "2":
                cont[relativebase+c] = d + e
            else:
                cont[c] = d + e
            x = x+4
        if instruction == "02":
            if value[0] == "2":
                cont[relativebase+c] = d * e
            else:
                cont[c] = d * e
            x = x+4
        if instruction == "03":
            print("Please enter input variable: ")
            inputvariable = input()
            if value[0] == "2":
                cont[relativebase+a] = int(inputvariable)
            else:
                cont[a] = int(inputvariable)
            x = x+2
        if instruction == "04":
            answer.append(d)
            x = x+2
        if instruction == "05":
            if d != 0:
                x = e
            else:
                x = x+3
        if instruction == "06":
            if d == 0:
                x = e
            else:
                x = x+3
        if instruction == "07":
            if d < e:
                if value[0] == "2":
                    cont[relativebase+c] = 1
                else:
                    cont[c] = 1
            else:
                if value[0] == "2":
                    cont[relativebase+c] = 0
                else:
                    cont[c] = 0
            x = x+4
        if instruction == "08":
            if d == e:
                if value[0] == "2":
                    cont[relativebase+c] = 1
                else:
                    cont[c] = 1
            else:
                if value[0] == "2":
                    cont[relativebase+c] = 0
                else:
                    cont[c] = 0
            x = x+4
        if instruction == "09":
            relativebase += d
            x = x+2
            
    return answer


f = open("C:/Users/Tadhg/Documents/Day13.txt", "r+")
cont = f.read().split(",")
f.close()
cont = list(map(int, cont))
output = intcode(cont)

maxx = 0
maxy = 0
for i in range(0, len(output), 3):
    if output[i] > maxx:
        maxx = output[i]
    if output[i+1] > maxy:
        maxy = output[i+1]

grid = [];
for j in range(maxx+1):
    column=[];
    for i in range(maxy+1):
        column.append(0);
    grid.append(column);

for i in range(0, len(output), 3):
    grid[output[i]][output[i+1]] = output[i+2]

blockcount = 0
for i in range(maxy+1):
    for j in range(maxx+1):
        if grid[j][i] == 0:
            print(' ', end = '')
        if grid[j][i] == 1:
            print('|', end = '')
        if grid[j][i] == 2:
            print(chr(0x2588), end = '')
            blockcount += 1
        if grid[j][i] == 3:
            print('_', end = '')
            losey = i
        if grid[j][i] == 4:
            print('O', end = '')
            x = j
            y = i
    print()
print(blockcount)
xchange = 1
ychange = 1

while y <= losey:
    grid[x][y] = 0
    if grid[x][y+ychange] != 0 or grid[x+xchange][y] != 0:
        if grid[x][y+ychange] != 0:
            if grid[x][y+ychange] == 2:
                grid[x][y+ychange] = 0
            ychange = -ychange
        if grid[x+xchange][y] != 0:
            if grid[x+xchange][y] == 2:
                grid[x+xchange][y] = 0
            xchange = -xchange            
    if grid[x+xchange][y+ychange] != 0:
        if grid[x+xchange][y+ychange] == 2:
            grid[x+xchange][y+ychange] = 0
        xchange = -xchange
        ychange = -ychange
        
    x += xchange
    y += ychange
    grid[x][y] = 4

blockcount = 0
for i in range(maxy+1):
    for j in range(maxx+1):
        if grid[j][i] == 0:
            print(' ', end = '')
        if grid[j][i] == 1:
            print('|', end = '')
        if grid[j][i] == 2:
            print(chr(0x2588), end = '')
            blockcount += 1
        if grid[j][i] == 3:
            print('_', end = '')
        if grid[j][i] == 4:
            print('O', end = '')
    print()

print(blockcount)

