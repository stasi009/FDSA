
def decrease_del(counts,v):
    newcount = counts[v]-1
    if newcount > 0:
        counts[v] = newcount
    else:
        del counts[v]    

def pair_sum(arr,k):
    counts = {}
    for v in arr:
        counts[v] = counts.get(v,0)+1

    pairs = []
    for v in arr:
        conjugate = k-v

        if v in counts and conjugate in counts:
            pairs.append((v,conjugate) if v < conjugate else (conjugate,v))
            
            decrease_del(counts,v)
            decrease_del(counts,conjugate)

    return pairs

def sol(arr,k):
    pairs = pair_sum(arr,k)
    print "%d,%s"%(len(pairs),pairs)

sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
sol([1,2,3,1],3)
sol([1,3,2,2],4)