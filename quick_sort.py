def quicksort(arr):
    # Base case: If the array is empty or has a single element, it's already sorted.
    if len(arr) <= 1:
        return arr
    else:
        # Choosing the first element as the pivot.
        pivot = arr[0]

        # Partitioning phase:
        # 'less' will hold elements less than or equal to the pivot.
        less = [x for x in arr[1:] if x <= pivot]

        # 'greater' will hold elements greater than the pivot.
        greater = [x for x in arr[1:] if x > pivot]

        # Recursive calls and concatenation:
        # The function is called recursively on the 'less' and 'greater' sub-arrays.
        # The returned arrays are then concatenated with the pivot in between.
        # This ensures that elements less than the pivot are before it, and those
        # greater are after it in the final array.
        return quicksort(less) + [pivot] + quicksort(greater)