from random import randint

def createCircle(width,height,a,b,r,mcIter,map01):
    mcColor = 100
    
    # Create a white-filled circle
    mapCount = 0
    for y in range(0,height-1):
        for x in range(0,width-1):
            if abs((x-a)**2+(y-b)**2) <= r**2:
                map01[y,x] = 255
                mapCount = mapCount + 1
    
    # MC Calculation
    mc = 0
    while mc < mcIter:
        i = randint(0,height-1)
        j = randint(0,width-1)
        if map01[i,j] == mcColor:
            while map01[i,j] == mcColor:
                i = randint(0,height-1)
                j = randint(0,width-1)
            map01[i,j] = mcColor
        else:
            map01[i,j] = mcColor
        mc = mc+1
    
    pixIn = 0
    # Calculate the results
    for y in range(0,height-1):
        for x in range(0,width-1):
            if abs((x-a)**2+(y-b)**2) <= r**2 and map01[y,x] == mcColor:
                pixIn = pixIn+1
    
    pixPercent = (pixIn/mcIter)*100
    
    return pixIn, pixPercent;

    