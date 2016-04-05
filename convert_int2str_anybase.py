
"""
Converting an Integer to a String in Any Base
"""

def int2string1(n,base):

    if n < base:
        return [n]
    else:
        q,r = divmod(n,base)
        a = int2string(q,base)
        a.append(r)
        return a

def int2string2(n,base):

    def __convert(n,base,representation):
        if n<base:
            representation.append(n)
        else:
            q,r = divmod(n,base)
            representation.append(r)
            __convert(q,base,representation)

    a = []
    __convert(n,base,a)
    return a[::-1]

def int2string_while():
    pass

int2string = int2string2
int2string(10,2)

        