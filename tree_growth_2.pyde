import tree

root = None 
pause = False

def setup():
    global root
    size(1000, 1000)
    background(255)
    frameRate(4)
    root = tree.Node(PVector(width/2, height), PVector(width/2, height - 10))

def draw():
    global root
    global pause
    if not pause:
        background(255)
        root.draw()
        root.update()
        saveFrame("tree_4_####.jpg")
        
def mouseClicked():
    global pause
    pause = not pause
    
 
