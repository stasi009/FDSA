
def binary_search(a,x,comparer=lambda e1,e2: e1 - e2):
    head = 0
    tail = len(a) - 1

    if comparer(x,a[head]) < 0:
        return False,head
    elif comparer(x,a[tail]) > 0:
        return False,tail + 1

    while tail - head > 1:
        middle = (head + tail) // 2
        # don't check > or <, but >= or <=
        # consider the case there are duplicates in the array
        assert a[middle] >= a[head] and a[middle] <= a[tail],"invariant condition"

        distance = comparer(x,a[middle])
        if distance == 0:
            return True,middle
        # !!! notice cannot be 'T=M-1' or 'T=H+1'
        # !!! because from x<a[M], we cannot guarantee x<a[M-1]
        elif distance < 0: # x< a[middle]
            tail = middle
        else:# x> a[middle]
            head = middle

    assert tail-head==1,"impossible to be 0"
    if comparer(a[head], x) == 0:
        return True,head
    elif comparer(a[tail],x) == 0:
        return True,tail
    else:
        assert x > a[head] and x < a[tail],"invariant condition"
        return False,tail # if we insert, the insert position







