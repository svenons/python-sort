def loop_control_example(arr):
    for i in arr:
        print(i)  # Loop control: iterating over each element of the array


def factorial(n):
    if n == 0:
        return 1  # Base case for recursion
    else:
        return n * factorial(n - 1)  # Recursive call

    # Example usage:
    #print(factorial(5))  # Outputs 120, which is 5!
