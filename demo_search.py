
def binary_search(a,x):
    head = 0
    tail = len(a) - 1

    if x < a[head]:         return False,head
    elif x > a[tail]:       return False,tail + 1

    while tail - head > 1:
        middle = (head + tail) // 2

        if x == a[middle]:
            return True,middle
        elif x < a[middle]: 
            tail = middle
        else:# x> a[middle]
            head = middle

    if a[head] == x:
        return True,head
    elif a[tail] == x:
        return True,tail
    else:
        return False,tail # if we insert, the insert position

if __name__ == "__main__":
    v = int(raw_input("value to search: "))
    N = int(raw_input("total length: "))
    txt_array = raw_input("array of ints: ")
    values = [int(s) for s in txt_array.split(' ')]

    found,index = binary_search(values,v)
    if found:
        print index
    else:
        print "%d cannot be found"%v
