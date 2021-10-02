f = open("C:/Users/Tadhg/Documents/Day16.txt", "r+")
cont = f.read()
f.close()
cont = list(map(int, cont))

count = 0
for i in cont:
    count+=1

inputlist = cont
for x in range(100):

    output = ""
    for i in range(count):
        countmultiplier = 0
        multiplybasearray = [None]* (4*(i+1))
        for j in range(i+1):
            multiplybasearray[countmultiplier] = 0
            countmultiplier += 1
        countmultiplier = 0
        for j in range(i+1):
            multiplybasearray[i+1 + countmultiplier] = 1
            countmultiplier += 1
        countmultiplier = 0
        for j in range(i+1):
            multiplybasearray[2*(i+1) + countmultiplier] = 0
            countmultiplier += 1
        countmultiplier = 0
        for j in range(i+1):
            multiplybasearray[3*(i+1) + countmultiplier] = -1
            countmultiplier += 1

        multiplyarray = [None]*count
        for j in range(count):
            if 1 + j%(4*countmultiplier) == 4*countmultiplier:
                multiplyarray[j] = multiplybasearray[0]
            else:
                multiplyarray[j] = multiplybasearray[1+j%(4*countmultiplier)]
            
        sum = 0
        for y in range(count):
            sum += inputlist[y]*multiplyarray[y]
        output += str(sum)[-1]

    inputlist = list(map(int, output))

print(output)

        

    

    
    
