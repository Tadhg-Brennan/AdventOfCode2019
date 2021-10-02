import math

f = open("C:/Users/Tadhg/Documents/Day10.txt", "r+");
contents = f.read().splitlines();
f.close()

cont = list(contents)

grid = []
icount = 0
jcount = 0

for i in cont[0]:
    column = []
    for j in cont:
        column.append(0)
    grid.append(column)

for i in cont:
    jcount = 0
    for j in cont[icount]:
        grid[jcount][icount] = j
        jcount += 1
    icount += 1

class asteroid:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
outputs =[]
asteroids = []
angle = 0;
icount = 0
for i in cont:
    jcount = 0
    for j in cont[icount]:
        if grid[jcount][icount] == '#':
            asteroidcount = 0
            angles = []
            asteroids = []
            icount1 = 0
            for i in cont:
                jcount1 = 0
                for j in cont[icount1]:
                    if grid[jcount1][icount1] == '#':
                        if icount == icount1:
                            if jcount < jcount1:
                                angle = math.pi/2
                            if jcount > jcount1:
                                angle = 3*math.pi/2
                        elif jcount == jcount1:
                            if icount > icount1:
                                angle = 0
                            if icount < icount1:
                                angle = math.pi
                        else:
                            angle = math.atan2(abs(jcount1-jcount),abs(icount1-icount))
                            if jcount1>jcount and icount1>icount:
                                angle = math.pi - angle
                            if jcount1<jcount and icount1>icount:
                                angle = math.pi + angle
                            if jcount1<jcount and icount1<icount:
                                angle = (2*math.pi) - angle   
                        if angle not in angles:
                            asteroidcount += 1
                            angles.append(angle)
                            asteroids.append(asteroid(jcount1, icount1, angle))
                    jcount1 += 1
                icount1 += 1
            outputs.append(asteroidcount)
            if asteroidcount == 253:
                angles.sort()
                icounta = 0
                for i in angles:
                    icounta +=1
                    if icounta == 200:
                        answerangle = i
                for i in asteroids:
                    if i.angle == answerangle:
                        print(jcount, icount)
                        print(i.x, i.y)
                        stepdivisor = math.gcd(jcount-i.x, icount-i.y)
                        asteroidcheck = False
                        xanswer = jcount
                        yanswer = icount
                        while not asteroidcheck:
                            xanswer = int(xanswer - ((jcount-i.x)/stepdivisor))
                            yanswer = int(yanswer - ((icount-i.y)/stepdivisor))
                            if grid[xanswer][yanswer] == "#":
                                asteroidcheck = True
                        print(xanswer, yanswer)
                            
                       
                            
        jcount += 1
    icount += 1
