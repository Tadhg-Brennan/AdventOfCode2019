f = open("C:/Users/Tadhg/Documents/Day16.txt", "r+")
cont = f.read()
f.close()
cont = list(map(int, cont))

count = 0
for i in cont:
    count+=1
inputlist = [None] *(count*10000)

for i in range(count*10000):
    inputlist[i] = cont[i%count]

offset = int("".join(map(str, inputlist))[:7])
print(offset)

print("".join(map(str, inputlist))[offset:offset+8])

inputlist = inputlist[offset:]

count=0
for i in inputlist:
    count+=1

for x in range(100):

    output = [None]*count            
    sum = 0
    loopcount = 0

    for i in range(count):
        loopcount += 1
        sum += inputlist[-loopcount]
        output[-loopcount] = int(str(sum)[-1]) 

    inputlist = output

print(output[:8])

        

    

    
    
