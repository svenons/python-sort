def binarysearch(arr, target):
    """
    Perform binary search on a sorted array.
    Returns the index of the target if found, otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid  # Target found
        if guess > target:
            high = mid - 1  # Target is in the left half
        else:
            low = mid + 1   # Target is in the right half

    return -1  # Target not found