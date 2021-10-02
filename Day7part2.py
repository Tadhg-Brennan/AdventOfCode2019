def intcode(cont, phasesetting, inputsignal, x, inputcount):
    class Output:
        def __init__(self, signal, x, cont):
            self.signal = signal
            self.x = x
            self.cont = cont
    instruction = "00"
    while instruction != "99":
        value = str(cont[x]).zfill(5)
        instruction = value[3:]

        if instruction != "99":
            a = cont[x+1]
            if instruction != "03" and instruction != "04":
                b = cont[x+2]
                c = cont[x+3]
 
        if instruction != "03" and instruction != "04" and instruction != "99":
        
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
            if inputcount > 1:
                inputvariable = inputsignal
            cont[a] = int(inputvariable)
            x = x+2
        if instruction == "04":
            x = x+2
            output = Output(cont[a], x, cont)
            return output
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
    output = Output("STOP", x, cont)
    return output
    
f = open("C:/Users/Tadhg/Documents/Day7.txt", "r+")
cont = f.read().split(",")
f.close()
cont = list(map(int, cont))
print("Please enter input signal: ")
inputsignal = input()

outputs = []
eoutputs = []
for a in range(5,10):
    for b in [b for b in range(5,10) if b!= a]:
        for c in [c for c in range(5,10) if c!=a and c!=b]:
            for d in [d for d in range(5,10) if d!=a and d!=b and d!=c]:
                for e in [e for e in range(5,10) if e!=a and e!=b and e!=c and e!=d]:

                    inputcount = 0
                    x = aX = bX = cX = dX = eX = 0
                    acont = bcont = ccont = dcont = econt = cont
                    ainput = inputsignal
                    outputsignal = 0
                    while outputsignal != "STOP":
                        
                        aoutput = intcode(acont, a, ainput, aX, inputcount)
                        outputsignal = aoutputsignal = aoutput.signal
                        aX = aoutput.x
                        acont = aoutput.cont
                        boutput = intcode(bcont, b, aoutputsignal, bX, inputcount)
                        outputsignal = boutputsignal = boutput.signal
                        bX = boutput.x
                        bcont = boutput.cont
                        coutput = intcode(ccont, c, boutputsignal, cX, inputcount)
                        outputsignal = coutputsignal = coutput.signal
                        cX = coutput.x
                        ccont = coutput.cont
                        doutput = intcode(dcont, d, coutputsignal, dX, inputcount)
                        outputsignal = doutputsignal = doutput.signal
                        dX = doutput.x
                        dcont = doutput.cont
                        eoutput = intcode(econt, e, doutputsignal, eX, inputcount)
                        outputsignal = ainput = eoutputsignal = eoutput.signal
                        eX = eoutput.x
                        econt = eoutput.cont
                        inputcount += 1
                        eoutputs.append(eoutputsignal)

                    outputs.append(eoutputs[-2])
    
print(max(outputs))
