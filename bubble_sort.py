def bubblesort(list):
    for x in range(len(list)-1,0,-1):
        for y in range(x):
            if list[y]>list[y+1]:
                temp = list[y]
                list[y] = list[y+1]
                list[y+1] = temp