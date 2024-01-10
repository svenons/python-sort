import random
import os
filepath = os.path.dirname(os.path.abspath(__file__))
file = filepath + "\\words.txt"

def numbers():
    numbers.list = []
    for a in range(0, 100):
        cipars = random.randrange(1, 1000)
        numbers.list.append(cipars)

    return numbers.list

def words():
    words.glist = []
    with open(file) as f:
        wordsi = f.readlines()
        for x in wordsi:
            x = x.replace("\n", "")
            if len(x) > 4:
                if len(x) < 8:
                    words.glist.append(x)
    
    words.list = []
    for x in range(0, 100):
        vards = random.choice(words.glist)
        words.list.append(vards)
    
    return words.list

from bubble_sort import bubblesort
from insertion_sort import insertionsort

#print(insertionsort(['Sylvia', 'Nancy', 'Lois', 'Alice']))
