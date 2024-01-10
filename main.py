from data import numbers
from data import words

from bubble_sort import bubblesort
from insertion_sort import insertionsort
from merge_sort import mergesort
from quick_sort import quicksort
from selection_sort import selectionsort
from shell_sort import shellsort

import os
clear = lambda: os.system('cls')
from timeit import default_timer as timer
clear()

## DISABLE THE CHOICE OF ALGORITHM AND DATA BY SETTING TO FALSE
run = True

## ADD MORE ALGORITHMS HERE
algoritms = ["bubble", "insertion", "selection", "merge", "quick", "shell"]

def choose(arr):
    while True:
        print("Choose between the following: \n")
        print("0. exit the choice")
        for i in range(len(arr)):
            print(f"{i+1}. {arr[i]}")
        choice = input("\n> ")
        try:
            choice = int(choice)
        except:
            choice = str(choice)
        if choice == 0 or choice == "exit":
            exit()
        if not (choice in range(1, len(arr)+1) or choice in arr):
            continue
        else:
            if type(choice) == int:
                return choice-1
            if type(choice) == str:
                return arr.index(choice)
        
if run:
    data = choose(["numbers", "words"])
    algo = choose(algoritms)
    algoritm = algoritms[algo]
    data = ["numbers", "words"][data]
    if data == "numbers":
        arr = numbers()
    if data == "words":
        arr = words()
    if algoritm == "bubble":
        start = timer()
        newarr = bubblesort(arr)
    if algoritm == "insertion":
        start = timer()
        newarr = arr = insertionsort(arr)
    if algoritm == "selection":
        start = timer()
        newarr = selectionsort(arr)
    if algoritm == "merge":
        start = timer()
        newarr = mergesort(arr)
    if algoritm == "quick":
        start = timer()
        newarr = quicksort(arr)
    if algoritm == "shell":
        start = timer()
        newarr = shellsort(arr)
    end = timer()
    time = end - start
    print(f"\nSorting took {time} seconds\n\n Original array: \n {arr} \n\n New array {newarr}")
    exit()