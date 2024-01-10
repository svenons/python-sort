def shellsort(arr):
    n = len(arr)
    gap = n // 2  # Initialize the gap

    # Start with a big gap, then reduce the gap
    while gap > 0:
        # Do a gapped insertion sort for this gap size.
        # The first gap elements arr[0..gap-1] are already in gapped order
        # keep adding one more element until the entire array is gap sorted
        for i in range(gap, n):
            # add arr[i] to the elements that have been gap sorted
            # save arr[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # put temp (the original arr[i]) in its correct location
            arr[j] = temp
        gap //= 2  # Reduce the gap
    return arr