def mergesort(list):
    if len(list) > 1:
        vidus = len(list) // 2
        sak = list[:vidus]
        beig = list[vidus:]
        mergesort(sak)
        mergesort(beig)
        x = 0
        y = 0
        z = 0
        while x < len(sak) and y < len(beig):
            if sak[x] < beig[y]:
                list[z] = sak[x]
                x += 1
            else:
                list[z] = beig[y]
                y += 1
            z += 1
        
        while x < len(sak):
            list[y] = sak[x]
            x += 1
            z +=1

        while y < len(beig):
            list[z] = beig[y]
            y += 1
            z += 1