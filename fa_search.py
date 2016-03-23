
def binary_search(a,x,comparer=lambda e1,e2: e1 - e2):
    head = 0
    tail = len(a) - 1

    if comparer(x,a[head]) < 0:
        return False,head
    elif comparer(x,a[tail]) > 0:
        return False,tail + 1

    while tail - head > 1:
        middle = (head + tail) // 2

        distance = comparer(x,a[middle])
        if distance == 0:
            return True,middle
        elif distance < 0: # x< a[middle]
            tail = middle
        else:# x> a[middle]
            head = middle

    if comparer(a[head], x) == 0:
        return True,head
    elif comparer(a[tail],x) == 0:
        return True,tail
    else:
        return False,tail # if we insert, the insert position




