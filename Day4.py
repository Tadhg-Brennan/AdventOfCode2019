x = 353096;
count = 0;

while x <= 843212:

    matched = False
    decreased = False
    stringx = str(x)
    for i in range(5):
        
        prev = stringx[i]
        curr = stringx[i+1]
        
        if int(curr) < int(prev):
            decreased = True

        if curr == prev:

            if i==0:
                if stringx[i+2] != curr:
                    matched = True

            if i==4:
                if stringx[i-1] != curr:
                    matched = True

            if i>0 and i<4:
                if stringx[i-1] != curr and stringx[i+2] != curr:
                    matched = True

    if matched == True and decreased == False:
        count += 1;

    x += 1

print(count)
