
"""
Find next greater number with same set of digits
"""

def swap(ar,i,j):
    temp = ar[i]
    ar[i] = ar[j]
    ar[j] = temp
    
# ar is descending from head to tail
# allow there may be duplicates
def find_next_larger(ar,v,head,tail):
    assert ar[head] > v
    if ar[tail] > v:
        return tail
    
    while tail - head > 1:
        middle = (head+tail)//2
        if v >= ar[middle]:
            tail = middle
        else: # v < ar[middle]
            head = middle
            
    if ar[head] > ar[tail]:    
        return head # next larger
    else:
        assert ar[head] == ar[tail]
        return tail

def reverse(ar,head,tail):
    while head < tail:
        swap(ar,head,tail)
        head += 1
        tail -= 1

def next_permuation(ar):
    # ------------ search from last position backwards
    # ------------ find the first position which violates the descending order
    i = len(ar)-2 # position which violates the descending order
    while i >=0 and ar[i] >= ar[i+1]:
        i -= 1
        
    if i < 0:
        return "no answer"
    else:
        j = find_next_larger(ar,ar[i],i+1,len(ar)-1)      
        swap(ar,i,j)
        reverse(ar,i+1,len(ar)-1)
        return "".join(ar)
        
with open("nlp_my_output.txt","wt") as outf:
    with open("nlp_input.txt","rt") as inf:
        inf.readline() # read the first line which is total number

        for index,line in enumerate(inf):
            line = line.strip()
            nextlarger = next_permuation(list(line))
            print "%d-th '%s'--->'%s'"%(index+1,line,nextlarger)
            outf.write(nextlarger+"\n")
