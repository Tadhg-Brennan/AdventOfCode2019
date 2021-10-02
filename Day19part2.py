def intcode(cont, xinput, yinput):
    x = 0
    count = 0
    relativebase = 0
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
            count+=1
            if count==1:
                inputvariable = xinput
            if count==2:
                inputvariable = yinput

            if value[2] == "2":
                cont[relativebase+a] = int(inputvariable)
            else:
                cont[a] = int(inputvariable)
            x = x+2
        if instruction == "04":
            return d  
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

grid = []
for j in range(50):
    column=[];
    for i in range(50):
        column.append(" ");
    grid.append(column);
    
f = open("C:/Users/Tadhg/Documents/Day19.txt", "r+")
cont = f.read().split(",")
f.close()
cont = list(map(int, cont))

i = 101
j = 0
check = False
while check == False:
    while check == False:
        f = open("C:/Users/Tadhg/Documents/Day19.txt", "r+")
        cont = f.read().split(",")
        f.close()
        cont = list(map(int, cont))
        result = intcode(cont,j,i)
        if result == 1:
            f = open("C:/Users/Tadhg/Documents/Day19.txt", "r+")
            cont = f.read().split(",")
            f.close()
            cont = list(map(int, cont))
            topleft = intcode(cont, j, i-99)
            if topleft == 1:
                f = open("C:/Users/Tadhg/Documents/Day19.txt", "r+")
                cont = f.read().split(",")
                f.close()
                cont = list(map(int, cont))
                topright = intcode(cont, j+99, i-99)
                if topright == 1:
                    check = True
            break
        if check == False:
            j+=1
    if check == False:
        i+=1
        
print(j*10000 + i-99)
