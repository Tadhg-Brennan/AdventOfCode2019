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


stepthrough1(wirea, grid);
stepthrough2(wireb, grid);

manhattans = []

for i in intersections:
    manhattans.append(abs(i[0]) + abs(i[1]))

print(min(manhattans))
