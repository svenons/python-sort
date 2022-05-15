def shellsort(list):
    garums = len(list)
    vidus = garums//2
    while vidus > 0:
        for x in range(vidus, garums):
            pagaidu = list[x]
            y = x
            while y >= vidus and list[y-vidus] > pagaidu:
                list[y] = list[y-vidus]
                y -= vidus
            list[y] = pagaidu
        vidus //= 2