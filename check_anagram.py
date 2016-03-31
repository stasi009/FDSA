
import string

check_characters = string.digits + string.ascii_lowercase
check_indices = [ord(e) for e in check_characters]

"""
above methods use two arrays for holding counts
actually we can use just one, because we don't care the actual number in the counts array
but just the difference
"""
def anagram(s1,s2):
    counts = [0 for i in xrange(128)]

    for c in s1:
        counts[ord(c.lower())] +=1

    for c in s2:
        counts[ord(c.lower())] -=1

    for index in check_indices:
        if counts[index] != 0:
            return False
    return True

class Version1(object):
    def count_characters(s):
        counts = [0 for i in xrange(128)]
        for c in s:
            counts[ord(c.lower())] += 1
        return counts

    def anagram(s1,s2):
        counts1 = count_characters(s1)
        counts2 = count_characters(s2)

        for index in check_indices:
            if counts1[index] != counts2[index]:
                return False
        return True

anagram('dog','god')
anagram('clint eastwood','old west action')
anagram('aa','bb')
anagram('hi man','hi     man')