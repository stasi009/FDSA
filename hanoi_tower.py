
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
    __move(N,"L","R","M")

move(3)

############################## print out pole status at each time
class Pole(object):
    def __init__(self,name,N=0):
        self.name = name
        self.items = range(N,0,-1)

    def push(self,e):
        self.items.append(e)

    def pop(self):
        return self.items.pop() # pop from tail only O(1)

    def display(self):
        print "%s: %s"%(self.name," ".join((str(e) for e in self.items)))

class HanoiTower(object):
    def __init__(self,N):
        self.N = N
        self.poles = [Pole("L",N),Pole("M"),Pole("R")]
        self.counter = 0

    def display(self):
        for p in self.poles:                
            p.display()

    def __move(self,n,frompole,topole,withpole):
        if n>=1:
            self.__move(n-1,frompole,withpole,topole)
            
            self.counter +=1
            top = frompole.pop()
            assert top == n # the last one
            topole.push(top)
            print "\n[%-3dth] disk#%-3d: %s ===> %s"%(self.counter,top,frompole.name,topole.name)
            self.display()

            self.__move(n-1,withpole,topole,frompole)

    def move(self):
        self.display()
        self.__move(self.N,self.poles[0],self.poles[2],self.poles[1])


ht = HanoiTower(10)
ht.move()



