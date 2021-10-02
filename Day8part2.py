f = open("C:/Users/Tadhg/Documents/Day8.txt", "r+");
contents = f.read();
f.close()

cont = list(contents)
cont = list(map(int, cont))
x=0
layer = []
answer = [2 for x in range(25*6)]
gridanswer = []
for i in range(25):
    column =[]
    for j in range(6):
        column.append(0)
    gridanswer.append(column)

for i in range(round(len(cont)/(25*6))):
    x+=25*6
    layer.append(cont[x-(25*6):x])  

for i in layer:
    count = 0
    for j in i:
        if j!=2 and answer[count]==2:
            answer[count] = j
        count+=1

count = 0
for i in answer:
    if i == 0:
        gridanswer[count%25][int(count/25)] = chr(0x2588)
    if i == 1:
        gridanswer[count%25][int(count/25)] = " "
    count+=1

for i in range(6):
    for j in range(25):
        print(gridanswer[j][i], end = '')
    print()
