f = open("C:/Users/tadhg.brennan/Documents/Day2.txt", "r+");
contents = f.readlines();
wirea = contents[0].split(",");
wireb = contents[1].split(",");

grid = [];
for j in range(10000):
    column=[];
    for i in range(10000):
        column.append(0);
    grid.append(column);
    
intersections = [];
counts = [];

def stepthrough1(wire, grid):

    x = 0;
    y = 0;
    for i in wire:

        movex = 0;
        movey = 0;        
        
        if i[0] == "L":
            movex = -1;
        if i[0] == "R":
            movex = 1;
        if i[0] == "U":
            movey = 1;
        if i[0] == "D":
            movey=-1;

        distance = int(i[1:]);

        for j in range(distance):
            x += movex;
            y += movey;

            grid[x][y] = 1;

        

def stepthrough2(wire, grid):

    x = 0;
    y = 0;
    for i in wire:

        movex = 0;
        movey = 0;        
        
        if i[0] == "L":
            movex = -1;
        if i[0] == "R":
            movex = 1;
        if i[0] == "U":
            movey = 1;
        if i[0] == "D":
            movey=-1;

        distance = int(i[1:]);

        for j in range(distance):
            x += movex;
            y += movey;
            
            if grid[x][y] == 1:
                grid[x][y] = 2;
                intersections.append([x, y]);
            else:
                grid[x][y] = 1;


def stepthrough3(wire, grid):

    x = 0;
    y = 0;
    count = 0;
    array = [];
    for i in wire:

        movex = 0;
        movey = 0;        
        
        if i[0] == "L":
            movex = -1;
        if i[0] == "R":
            movex = 1;
        if i[0] == "U":
            movey = 1;
        if i[0] == "D":
            movey=-1;

        distance = int(i[1:]);

        for j in range(distance):
            x += movex;
            y += movey;
            count += 1;

            if [x, y] in intersections:
                array.append([x, y, count])

    return array            

    

stepthrough1(wirea, grid);
stepthrough2(wireb, grid);
counta = stepthrough3(wirea, grid);
countb = stepthrough3(wireb, grid);

for i in counta:

    for j in countb:

        if j[0] == i[0] and j[1] == i[1]:

            counts.append(i[2] + j[2])


print(min(counts))
