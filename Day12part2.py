from math import gcd

class planet:
    def __init__(self, posx, posy, posz, velx, vely, velz, origx, origy, origz, xback, yback, zback):
        self.posx = posx
        self.posy = posy
        self.posz = posz
        self.velx = velx
        self.vely = vely
        self.velz = velz
        self.origx = origx
        self.origy = origy
        self.origz = origz
        self.xback = xback
        self.yback = yback
        self.zback = zback

f = open("C:/Users/Tadhg/Documents/Day12.txt", "r+")
cont = f.readlines()
f.close()
planets = []

for i in cont:
    coordinates = i.replace(' ', '').replace('\n', '').replace('<', '').replace('>', '').replace('x', '').replace('y', '').replace('z', '').replace('=', ''). split(',')
    planets.append(planet(int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), 0,0,0, int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), False, False, False))

steps = 0
xperiod = 0
yperiod = 0
zperiod = 0

while xperiod == 0 or yperiod == 0 or zperiod == 0:

    steps += 1
    for i in planets:

        xchange = 0
        ychange = 0
        zchange = 0
    
        for j in planets:

            if i.posx > j.posx:
                xchange += -1
            if i.posx < j.posx:
                xchange += 1
            if i.posy > j.posy:
                ychange += -1
            if i.posy < j.posy:
                ychange += 1
            if i.posz > j.posz:
                zchange += -1
            if i.posz < j.posz:
                zchange += 1

        i.velx += xchange
        i.vely += ychange
        i.velz += zchange

    for i in planets:
        i.posx += i.velx
        i.posy += i.vely
        i.posz += i.velz

        i.xback = False
        i.yback = False
        i.zback = False

        if i.posx == i.origx and i.velx == 0:
            i.xback = True
        if i.posy == i.origy and i.vely == 0:
            i.yback = True
        if i.posz == i.origz and i.velz == 0:
            i.zback = True

    xmatchcount = 0
    ymatchcount = 0
    zmatchcount = 0
    for i in planets:
        if i.xback == True:
            xmatchcount += 1
        if i.yback == True:
            ymatchcount += 1
        if i.zback == True:
            zmatchcount += 1

    if xmatchcount == 4 and xperiod == 0:
        xperiod = steps
        print(xperiod)
    if ymatchcount == 4 and yperiod == 0:
        yperiod = steps
        print(yperiod)
    if zmatchcount == 4 and zperiod == 0:
        zperiod = steps
        print(zperiod)

interim = xperiod*yperiod//gcd(xperiod,yperiod)
answer = zperiod*interim//gcd(zperiod, interim)

print(answer)
