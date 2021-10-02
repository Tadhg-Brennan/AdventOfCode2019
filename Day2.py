noun=0
verb=0
y=0

def intcode(cont):
    x = 0;
    while cont[x] !=99:
        a = cont[x+1]
        b = cont[x+2]
        c = cont[x+3]
        if cont[x] == 1:
            cont[c] = cont[a] + cont[b]
        if cont[x] == 2:
            cont[c] = cont[a] * cont[b]

        x = x+4

    return cont[0]

for i in range(100):
    noun = i;
    for j in range(100):
        verb = j;
        f = open("C:/Users/tadhg.brennan/Documents/Day2.txt", "r+")
        cont = f.read().split(",")
        f.close()
        cont = list(map(int, cont))
        cont[1] = noun
        cont[2] = verb
        y = intcode(cont)
        if y == 19690720:
            break
    if y == 19690720:
        break

print(100*noun + verb)
