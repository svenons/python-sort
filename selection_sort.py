def selectionsort(list):
    for x in range(len(list)):
        minx = x
        for y in range(x+1, len(list)):
            if list[minx] > list[y]:
                minx = y
    list[x], list[minx] = list[minx], list[x]
