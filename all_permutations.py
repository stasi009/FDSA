
def __insert(arr,pos,x):
    expanded = [None for _  in xrange(len(arr)+1)]
    for idx in xrange(0,pos):
        expanded[idx] = arr[idx]
        
    expanded[pos] = x
    
    for idx in xrange(pos+1,len(arr)+1):
        expanded[idx] = arr[idx-1] 

    return expanded

def __permutation(characters):
    N = len(characters)

    if N==1:
        return [[characters[0]]]

    ch = characters.pop()
    permutations = __permutation(characters)

    results = []
    for pcharacters in permutations:
        # pcharacters isn't a string, but a list
        for idx in xrange(len(pcharacters)+1):
            # insert at idx position
            results.append(__insert(pcharacters,idx,ch))

    return results

def all_permutations(s):
    characters = list(s)
    permutations = __permutation(characters)
    return ["".join(pchs) for pchs in permutations]    

if __name__ == "__main__":
    print all_permutations("abc")        
