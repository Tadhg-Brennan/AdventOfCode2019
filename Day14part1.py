import math

class material:
    def __init__(self, name, equationquantity, components, quantityneeded, done, count, countloop):
        self.name = name
        self.equationquantity = equationquantity
        self.components = components
        self.quantityneeded = quantityneeded
        self.done = done
        self.count = count
        self.countloop = countloop

f = open("C:/Users/Tadhg/Documents/Day14.txt", "r+")
cont = f.read().splitlines()
f.seek(0)
contents = str(f.read())
f.close()

answer = 0
materials = []

for i in cont:
    io = i.split(" => ")
    output = io[1].split(' ')
    quantity = int(output[0])
    name = output[1]

    components = io[0].split(", ")
    if name == "FUEL":
        materials.append(material(name, quantity, components, 1, False, 0, 0))
    else:
        materials.append(material(name, quantity, components, 0, False, 0, 0))

for i in materials:
    count = contents.count(i.name)
    i.count = count-1 

notdone = True
while notdone:
    notdone = False
    for i in materials:
        if i.quantityneeded == 0 or i.count>i.countloop:
            notdone = True
        elif i.done == False: 
            for j in i.components:
                component = j.split(" ")
                quantityneededfromeq = int(component[0])*math.ceil(i.quantityneeded/i.equationquantity)
                componentname = component[1]
                if componentname == "ORE":
                    answer += quantityneededfromeq
                else:
                    for x in materials:
                        if componentname == x.name:
                            j = x
                    j.quantityneeded += quantityneededfromeq
                    j.countloop += 1
            i.done = True

print(answer)
            
        
