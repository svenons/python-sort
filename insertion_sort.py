def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j]:
            #print(arr)
            arr[j + 1] = arr[j]
            j -= 1
            #print(arr)
        arr[j + 1] = key
    return arr