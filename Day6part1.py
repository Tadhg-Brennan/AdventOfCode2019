f = open("C:/Users/Tadhg/Documents/Day6.txt", "r+");
contents = f.readlines();

planetlist = []
counter = 0

class planet:
    def __init__(child, name, parent):
        child.name = name
        child.parent = parent

for i in contents:

    j = i.split(")");
    parent = j[0].strip();    
    child = planet(j[1].strip(), parent)
    planetlist.append(child)

for i in planetlist:
    for j in planetlist:
        if j.name == i.parent:
            i.parent = j
            
for i in planetlist:
    counter += 1
    nextone = i.parent
    while nextone != str(nextone):
        nextone = nextone.parent
        counter += 1

print(counter)
        
        
        


    
