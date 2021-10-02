from operator import attrgetter

f = open("C:/Users/Tadhg/Documents/Day8.txt", "r+");
contents = f.read();
f.close()

cont = list(contents)
cont = list(map(int, cont))
x=0
layer = []
layeranswers=[]

for i in range(round(len(cont)/(25*6))):
    x+=25*6
    layer.append(cont[x-(25*6):x])

class Layer:
    def __init__(self, number, zerocount, answer):
        self.number = number
        self.zerocount = zerocount
        self.answer = answer    

for i in layer:
    zerocount = onecount = twocount = 0
    for j in i:
        if j == 0:
            zerocount+=1
        if j == 1:
            onecount+=1
        if j == 2:
            twocount+=1
    layeranswers.append(Layer(i, zerocount, onecount*twocount))

print(min(layeranswers, key=attrgetter('zerocount')).answer)
