def insertionsort(list):
    for x in range(1, len(list)):
        y = x - 1
        el = list[x]
    while (list[y] > el) and (y >= 0):
        list[y+1] = list[y]
        y = y - 1
        list[y+1] = el