
class Stack(object):

    def __init__(self,initstate = None):
        if initstate is None:  
            self.items = []
        else:
            self.items = initstate

    def push(self,e):
        self.items.append(e)

    def pop(self):
        return self.items.pop() # pop from tail only O(1)

    def peek(self):
        return self.items[len(self.items)-1]

    def __len__(self):
        return len(self.items)


s = Stack()
s.push(4)
s.push('dog')
s.peek()
s.pop()
len(s)

        