class output:
    def __init__(self, x, relativebase, output1, output2):
        self.relativebase = relativebase
        self.x = x
        self.output1 = output1
        self.output2 = output2
        

def intcode(cont, inputx, relativebase, x):
    
    outputcount = 0;
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
            inputvariable = inputx
            if value[0] == "2":
                cont[relativebase+a] = int(inputvariable)
            else:
                cont[a] = int(inputvariable)
            x = x+2
        if instruction == "04":
            outputcount += 1
            if outputcount == 1:
                output1 = d
            if outputcount == 2:
                output2 = d
                x = x+2
                return output(x, relativebase, output1, output2)
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
            
    return output(x, relativebase, "STOP", "STOP")


f = open("C:/Users/Tadhg/Documents/Day11.txt", "r+")
cont = f.read().split(",")
f.close()
cont = list(map(int, cont))
x=0
inputx = 0
relativebase = 0
paintcount = 0

grid = [];
for j in range(100):
    column=[];
    for i in range(100):
        column.append(0);
    grid.append(column);

currentdirection = "U"
positionx = 50
positiony = 50
thisoutput = output(x, relativebase, inputx, x)
paintedtiles = []

while thisoutput.output2 != "STOP":

    thisoutput = intcode(cont, inputx, relativebase, x)
    
    if thisoutput.output1 == 0 and grid[positionx][positiony] == 1:
        grid[positionx][positiony] = 0

    if thisoutput.output1 == 1 and grid[positionx][positiony] == 0:
        grid[positionx][positiony] = 1
        if 100*positionx + positiony not in paintedtiles:
            paintedtiles.append(100*positionx + positiony)

    xchange = 0
    ychange = 0

    if thisoutput.output2 == 0:
        if currentdirection == "U":
            direction = "L"
            xchange = -1
        if currentdirection == "L":
            direction = "D"
            ychange = -1
        if currentdirection == "D":
            direction = "R"
            xchange = 1
        if currentdirection == "R":
            direction = "U"
            ychange = 1
    if thisoutput.output2 == 1:
        if currentdirection == "U":
            direction = "R"
            xchange = 1
        if currentdirection == "L":
            direction = "U"
            ychange = 1
        if currentdirection == "D":
            direction = "L"
            xchange = -1
        if currentdirection == "R":
            direction = "D"
            ychange = -1

    currentdirection = direction
    positionx += xchange
    positiony += ychange
    inputx = grid[positionx][positiony]
    relativebase = thisoutput.relativebase
    x = thisoutput.x

for i in paintedtiles:
    paintcount += 1

print(paintcount)
