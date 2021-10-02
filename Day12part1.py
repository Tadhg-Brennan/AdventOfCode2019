class planet:
    def __init__(self, posx, posy, posz, velx, vely, velz):
        self.posx = posx
        self.posy = posy
        self.posz = posz
        self.velx = velx
        self.vely = vely
        self.velz = velz

f = open("C:/Users/Tadhg/Documents/Day12.txt", "r+")
cont = f.readlines()
f.close()
planets = []

for i in cont:
    coordinates = i.replace(' ', '').replace('\n', '').replace('<', '').replace('>', '').replace('x', '').replace('y', '').replace('z', '').replace('=', ''). split(',')
    print(coordinates)
    planets.append(planet(int(coordinates[0]), int(coordinates[1]), int(coordinates[2]), 0,0,0))

for i in range(1000):

    energy = 0
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

    for i in planets:
        energy += (abs(i.posx)+abs(i.posy)+abs(i.posz))*(abs(i.velx)+abs(i.vely)+abs(i.velz))

print(energy)
    
