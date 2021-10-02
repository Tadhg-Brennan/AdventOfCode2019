import random

def intcode(cont):
    x = 0;
    posx = 25
    posy = 25
    inputvariable = 1
    testcount = 0
    grid = [];
    pathvar = "o"
    for j in range(50):
        column=[];
        for i in range(50):
            column.append(" ");
        grid.append(column);
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
            if grid[posx][posy-1] == " ":
                inputvariable = 1
                pathvar = "o"
            elif grid[posx+1][posy] == " ":
                inputvariable = 4
                pathvar = "o"
            elif  grid[posx][posy+1] == " ":
                inputvariable = 2
                pathvar = "o"
            elif grid[posx-1][posy] == " ":
                inputvariable = 3
                pathvar = "o"
            else:
                viablepaths = 0
                if grid[posx][posy-1] == "o":
                    viablepaths += 1
                if grid[posx+1][posy] == "o":
                    viablepaths += 1
                if  grid[posx][posy+1] == "o":
                    viablepaths += 1
                if grid[posx-1][posy] == "o":
                    viablepaths += 1
                if viablepaths == 1:
                    if grid[posx][posy-1] == "o":
                        inputvariable = 1
                    elif grid[posx+1][posy] == "o":
                        inputvariable = 4
                    elif  grid[posx][posy+1] == "o":
                        inputvariable = 2
                    elif grid[posx-1][posy] == "o":
                        inputvariable = 3
                    pathvar = "#"
                if viablepaths > 1:
                    inputvariable = random.randint(1,4)
                
            if value[0] == "2":
                cont[relativebase+a] = int(inputvariable)
            else:
                cont[a] = int(inputvariable)
            x = x+2
        if instruction == "04":

            grid[posx][posy] = pathvar
            
            if inputvariable == 1:                
                if d == 1 or d == 2:
                    posy -= 1
                if d == 0:
                    grid[posx][posy-1] = "#"
            if inputvariable == 2:                
                if d == 1 or d == 2:
                    posy += 1
                if d == 0:
                    grid[posx][posy+1] = "#"
            if inputvariable == 3:                
                if d == 1 or d == 2:
                    posx -= 1
                if d == 0:
                    grid[posx-1][posy] = "#"
            if inputvariable == 4:                
                if d == 1 or d == 2:
                    posx += 1
                if d == 0:
                    grid[posx+1][posy] = "#"
            if d == 2:
                grid[posx][posy] = "S"
                return grid

            grid[posx][posy] = "R"

            if testcount == 1000000:
                for i in range(50):
                    for j in range(50):
                        print(grid[j][i], end ='')
                    print()
                testcount = 0


            testcount+=1
                
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

f = open("C:/Users/Tadhg/Documents/Day15.txt", "r+")
cont = f.read().split(",")
f.close()
cont = list(map(int, cont))
grid = intcode(cont)
count = 0
for i in range(50):
    for j in range(50):
        print(grid[j][i], end ='')
        if grid[j][i] == "o":
            count+=1
    print()

print(count)
