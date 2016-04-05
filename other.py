
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,200)
myWin.exitonclick()

def bubble_sort(ar):
    N = len(ar)
    for i in xrange(N-1):
        swaped = False
        
        for j in xrange(N-1-i):
            if ar[j] > ar[j+1]:
                temp = ar[j+1]
                ar[j+1] = ar[j]
                ar[j] = temp
                swaped = True

        if not swaped:
            break

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)
print alist