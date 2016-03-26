
MAX = 100
def count_sort(ar):
    ################ count
    counts = [0 for i in xrange(MAX)]
    for (v,s) in ar:
        counts[v] +=1
    ################ frequencies
    offsets = [None for i in xrange(MAX)]
    offsets[0] = 0
    for index in xrange(1,MAX):
        offsets[index] = offsets[index-1]+counts[index-1]
    ################ sort
    results = [None for i in xrange(len(ar))]
    for t in ar:
        v = t[0]
        results[ offsets[v] ] = t
        offsets[v] += 1
    return results
    
with open("count_sort_input.txt","rt") as inf:
    N = int(inf.readline())
    half = N//2
    ar = [None for i in xrange(N)]
    for index in xrange(1,N+1):
        segments = inf.readline().strip().split()
        assert len(segments)==2
        v = int(segments[0])
        s = segments[1] if index > half else '-'
        ar[index-1] = (v,s)

results = count_sort(ar)
print " ".join( (str(t[1]) for t in results) )