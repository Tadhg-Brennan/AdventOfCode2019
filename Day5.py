def intcode(cont):
    x = 0;
    instruction = "00"
    while instruction != "99":
        value = str(cont[x]).zfill(5)
        instruction = value[3:]

        if instruction != "99":
            a = cont[x+1]
            b = cont[x+2]
            c = cont[x+3]
 
        if instruction != "03" and instruction != "04":
        
            if value[2] == "0":
                d = cont[a]
            if value[2] == "1":
                d = a
            if value[1] == "0":
                e = cont[b]
            if value[1] == "1":
                e = b

        if instruction == "01":
            cont[c] = d + e
            x = x+4
        if instruction == "02":
            cont[c] = d * e
            x = x+4
        if instruction == "03":
            print("Please enter input variable: ")
            inputvariable = input()
            cont[a] = int(inputvariable)
            x = x+2
        if instruction == "04":
            print(cont[a])
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
                cont[c] = 1
            else:
                cont[c] = 0
            x = x+4
        if instruction == "08":
            if d == e:
                cont[c] = 1
            else:
                cont[c] = 0
            x = x+4


f = open("C:/Users/Tadhg/Documents/Day5.txt", "r+")
cont = f.read().split(",")
f.close()
cont = list(map(int, cont))
intcode(cont)
