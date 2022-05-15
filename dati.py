import random
import os
filepath = os.path.dirname(os.path.abspath(__file__))
words = filepath + "\\words.txt"

def cipari():
    cipari.list = []
    for a in range(0, 100):
        cipars = random.randrange(1, 1000)
        cipari.list.append(cipars)

def vardi():
    vardi.glist = []
    with open(words) as f:
        vardii = f.readlines()
        for x in vardii:
            x = x.replace("\n", "")
            if len(x) > 4:
                if len(x) < 8:
                    vardi.glist.append(x)
    
    vardi.list = []
    for x in range(0, 100):
        vards = random.choice(vardi.glist)
        vardi.list.append(vards)
