import random

def intcode(cont):
    x = 0;
    inputvariable = 1
    grid = [];
    for j in range(100):
        column=[];
        for i in range(100):
            column.append(" ");
        grid.append(column);
    j=0
    i=0
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
            print("input: ")
                
            if value[0] == "2":
                cont[relativebase+a] = int(inputvariable)
            else:
                cont[a] = int(inputvariable)
            x = x+2
        if instruction == "04":

            if d == 35:
                grid[j][i] = "#"
                j+=1
            if d == 46:
                grid[j][i] = "."
                j+=1
            if d == 60:
                grid[j][i] = "<"
                j+=1
            if d == 86:
                grid[j][i] = "V"
                j+=1
            if d == 62:
                grid[j][i] = ">"
                j+=1
            if d == 94:
                grid[j][i] = "^"
                j+=1
            if d == 10:
                j=0
                i+=1
                
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

    return grid

f = open("C:/Users/Tadhg/Documents/Day17.txt", "r+")
cont = f.read().split(",")
f.close()
cont = list(map(int, cont))
grid = intcode(cont)

cont[0] = 2
for i in range(100):
    for j in range(100):
        if grid[j][i] == "^":
            posx = j
            posy = i
            
fullanswer = ""
sum = 0
finished = False
while finished == False:
    if grid[posx][posy] == "^":
        if grid [posx][posy-1] == "#":
            grid[posx][posy] = "#"
            sum += 1
            posy += -1
            grid[posx][posy] = "^"
        elif grid[posx][posy-1] == "." or grid[posx][posy-1] == " " or posy == 0:
            fullanswer += str(sum)+","
            sum = 0
            if grid[posx-1][posy] == "#":
                fullanswer += "L,"
                grid[posx][posy] = "<"
            elif grid[posx+1][posy] == "#":
                fullanswer += "R,"
                grid[posx][posy] = ">"
            else:
                fullanswer += str(sum)
                finished = True
    elif grid[posx][posy] == "<":
        if grid [posx-1][posy] == "#":
            grid[posx][posy] = "#"
            sum += 1
            posx += -1
            grid[posx][posy] = "<"
        elif grid[posx-1][posy] == "." or grid[posx-1][posy] == " " or posx == 0:
            fullanswer += str(sum)+","
            sum = 0
            if grid[posx][posy+1] == "#":
                fullanswer += "L,"
                grid[posx][posy] = "V"
            elif grid[posx][posy-1] == "#":
                fullanswer += "R,"
                grid[posx][posy] = "^"
            else:
                fullanswer += str(sum)
                finished = True
    elif grid[posx][posy] == "V":
        if grid [posx][posy+1] == "#":
            grid[posx][posy] = "#"
            sum += 1
            posy += 1
            grid[posx][posy] = "V"
        elif grid[posx][posy+1] == "." or grid[posx][posy+1] == " ":
            fullanswer += str(sum)+","
            sum = 0
            if grid[posx-1][posy] == "#":
                fullanswer += "R,"
                grid[posx][posy] = "<"
            elif grid[posx+1][posy] == "#":
                fullanswer += "L,"
                grid[posx][posy] = ">"
            else:
                fullanswer += str(sum)
                finished = True
    elif grid[posx][posy] == ">":
        if grid [posx+1][posy] == "#":
            grid[posx][posy] = "#"
            sum += 1
            posx += 1
            grid[posx][posy] = ">"
        elif grid[posx+1][posy] == "." or grid[posx+1][posy] == " ":
            fullanswer += str(sum)+","
            sum = 0
            if grid[posx][posy-1] == "#":
                fullanswer += "L,"
                grid[posx][posy] = "^"
            elif grid[posx][posy+1] == "#":
                fullanswer += "R,"
                grid[posx][posy] = "V"
            else:
                fullanswer += str(sum)
                finished = True

A = "L,12,R,4,R,4"
B = "R,12,R,4,L,6,L,8,L,8"
C = "R,12,R,4,L,12,R,12,R,4,L,12"
fullanswer = fullanswer[2:-2].replace(A, "A").replace(B, "B").replace(C,"C")
finalanswer = fullanswer + ",10" + A + ",10" + B + ",10" + C + ",10"
finalanswer = finalanswer.replace("4","52").replace("6","54").replace("8","56").replace("1", "49").replace("2","50").replace(",","44").replace("R","82").replace("L","76").replace("A","65").replace("B","66").replace("C","67").replace("490","10")
print(list(finalanswer))    
