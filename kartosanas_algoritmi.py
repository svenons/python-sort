from heapq import merge
from sre_constants import NOT_LITERAL_IGNORE
from dati import cipari
from dati import vardi
from bubble_sort import bubblesort
from insertion_sort import insertionsort
from selection_sort import selectionsort
from merge_sort import mergesort
from quick_sort import quicksort
from shell_sort import shellsort

from timeit import default_timer as timer

# Kartosanas algoritmu testi atrodami zemāk, tomēr zemāk zem komentāriem uztaisiju mazu scriptu ar input, 
# lai vieglāk un slinkāk pārbaudīt manu darbu.
# Laika testēšanu implementēju ja lieto sortus caur šo algoritmu, nevis pašos algoritmos.

#cipari()
#print(cipari.list, "\n\n")
#vardi()
#print(vardi.list, "\n\n")

#bubblesort(cipari.list)
#bubblesort(vardi.list)
#print(cipari.list)
#print(vardi.list)

#insertionsort(cipari.list)
#print(cipari.list)
#insertionsort(vardi.list)
#print(vardi.list)

#selectionsort(cipari.list)
#selectionsort(vardi.list)
#print(cipari.list)
#print(vardi.list)

#mergesort(cipari.list)
#print(cipari.list)
#mergesort(vardi.list)
#print(cipari.list)

#quicksort(cipari.list)
#print(cipari.list)
#quicksort(vardi.list)
#print(vardi.list)

#shellsort(cipari.list)
#print(cipari.list)
#shellsort(vardi.list)
#print(vardi.list)

def dosort(list):
    while True:
        print('Izvelies sort metodi: \n   *ieraksti "bubble" prieks bubble_sort \n   *ieraksti "insertion" prieks insertion_sort \n   *ieraksti "selection" prieks selection_sort \n   *ieraksti "merge" prieks merge_sort \n   *ieraksti "quick" prieks quicksort \n   *ieraksti "shell" prieks shell_sort')
        ine = input("")
        if not ine in ["bubble", "insertion", "selection", "merge", "quick", "shell"]:
            continue
        else:
            print("Lists pirms kārtošanas: ", list, "\n")
            start = timer()
            if ine == "bubble":
                bubblesort(list)
            if ine == "insertion":
                insertionsort(list)
            if ine == "selection":
                selectionsort(list)
            if ine == "merge":
                mergesort(list)
            if ine == "quick":
                quicksort(list)
            if ine == "shell":
                shellsort(list)
            end = timer()
            laiks = end - start
            print(f"Lists pēc {ine} kārtošanas: ", list, f"\n\nSortošanas algoritms prasīja {laiks} sekundes")
            break

while True:
    print('Izvelies datus: \n   *ieraksti "vardi" prieks vardiem \n   *ieraksti "cipari" prieks cipariem')
    ine = input("")
    if not ine in ["cipari", "vardi"]:
        continue
    else:
        break

if ine == "cipari":
    cipari()
    dosort(cipari.list)
elif ine == "vardi":
    vardi()
    dosort(vardi.list)