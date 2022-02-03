import turtle

def findRepStr(n, d, b):
    result = []
    curMod = n
    #counter = 0
    found = set()
    if n >= d:
        print("Fraction greater than 1!")
        return([])
    while(not(curMod in found) or len(result) == 0):
        found.add(curMod)
        curMod *= b
        result.append(curMod//d)
        curMod %= d
        #counter += 1
        #print(curMod)
    return(result)

curStep = 60
curBase = 60
numList = findRepStr(1, 2**2, curBase)
print(numList)
if(sum(numList) % curBase == 0):
    print("Possibly Non-cyclic pattern! May need to force close.")
screen = turtle.Screen()
screen.screensize(10000,10000)
turtle.speed(1)
turtle.hideturtle()
for i in numList:
    turtle.left(i*(360/curBase) % 360)
    turtle.forward(curStep)
while(abs(turtle.xcor()) > 1 or abs(turtle.ycor()) > 1):
    for i in numList:
        turtle.left(i*(360/curBase) % 360)
        turtle.forward(curStep)
turtle.done()