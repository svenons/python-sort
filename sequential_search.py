def sequentialsearch(arr, target):
    """
    Sequentially search for the target in the list.
    Returns the index of the target if found, otherwise returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found, return the index
    return -1  # Target not found