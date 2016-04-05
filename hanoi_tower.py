
def __move(N,frompole,topole,withpole):
    """
    plate 1~N are on from pole
    we are going to move plate 1~N from 'frompole' to 'topole' via 'withpole'
    """
    if N == 1:
        print "%d: %s ==> %s"%(N,frompole,topole)# move directly
    else:
        __move(N-1,frompole,withpole,topole)
        print "%d: %s ==> %s"%(N,frompole,topole)
        __move(N-1,withpole,topole,frompole)


def move(N):
    pass
