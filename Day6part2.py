f = open("C:/Users/Tadhg/Documents/Day6.txt", "r+");
contents = f.readlines();

planetlist = []

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

YOUlist = []
SANlist = []
            
for i in planetlist:

    if i.name == "YOU":
        nextone = i.parent
        YOUlist.append(nextone)
        while nextone != str(nextone):
            nextone = nextone.parent
            YOUlist.append(nextone)
    if i.name == "SAN":
        nextone = i.parent
        SANlist.append(nextone)
        while nextone != str(nextone):
            nextone = nextone.parent
            SANlist.append(nextone)

icount = -1
for i in SANlist:
    icount += 1
    jcount = -1
    for j in YOUlist:
        jcount += 1
        if j == i:
            print(icount+jcount)

