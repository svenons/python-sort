def nodala(list, sak, beig):
    balsts = sak
    for x in range(sak+1, beig+1):
        if list[x] <= list[sak]:
            balsts += 1
            list[x], list[balsts], = list[balsts], list[x]
    list[balsts], list[sak] = list[sak], list[balsts]
    return balsts

def quicksort(list, sak=0, beig=None):
    if beig is None:
        beig = len(list) - 1
    def _quicksort(list, sak, beig):
        if sak >= beig:
            return
        balsts = nodala(list, sak, beig)
        _quicksort(list, sak, balsts-1)
        _quicksort(list, balsts+1, beig)
    return _quicksort(list, sak, beig)