def intcode(cont, phasesetting, inputsignal):
    outputarray = []
    x = 0;
    inputcount = 0;
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
            inputcount += 1
            if inputcount == 1:
                inputvariable = phasesetting
            if inputcount == 2:
                inputvariable = inputsignal
            cont[a] = int(inputvariable)
            x = x+2
        if instruction == "04":
            return cont[a]
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

f = open("C:/Users/Tadhg/Documents/Day7.txt", "r+")
cont = f.read().split(",")
f.close()
cont = list(map(int, cont))
print("Please enter input signal: ")
inputsignal = input()

outputs = []

for a in range(5): 
    aoutput = intcode(cont, a, inputsignal)
    for b in [b for b in range(5) if b!= a]:
        boutput = intcode(cont, b, aoutput)
        for c in [c for c in range(5) if c!=a and c!=b]:
            coutput = intcode(cont, c, boutput)
            for d in [d for d in range(5) if d!=a and d!=b and d!=c]:
                doutput = intcode(cont, d, coutput)
                for e in [e for e in range(5) if e!=a and e!=b and e!=c and e!=d]:
                    eoutput = intcode(cont, e, doutput)
                    outputs.append(eoutput)
print(max(outputs))
