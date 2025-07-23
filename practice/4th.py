def divisibleBy9 (n):
    digicount = 0
    for i in range(1,n+1):
        count = 0 
        for j in range(1,i+1):
            if(i % j == 0):
                count += 1
        if(count == 9):
            digicount += 1
    return digicount



print(divisibleBy9(100531665464864645))


    