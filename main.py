import pgzrun,random
from time import time


HEIGHT=600
WIDTH=800

satelites = []
number_of_satelite= 8
next_satelite= 0

lines= []
start_time = 0
total_time= 0
end_time=0

TITLE="satelites game"



def create_satelite():
    global start_time
    for i in range(0,number_of_satelite):
        satelite=Actor("satelite")
        x=random.randint(0,700)
        y=random.randint(0,550)
        satelite.pos=x,y
        satelites.append(satelite)
    start_time = time()

def draw():
    global total_time
    screen.clear()
    screen.blit("background", (0,0))
    number=1
    for satelite in satelites:
        satelite.draw()
        screen.draw.text(str(number), (satelite.pos[0], satelite.pos[1]+20))
        #adding to number
        number=number+1
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))
    if next_satelite < number_of_satelite:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    if next_satelite == 8:
        screen.draw.text("game is finished! good job",(300,300),fontsize=50)


def on_mouse_down(pos):
    print("you are in space")
    global next_satelite, lines
    if next_satelite < number_of_satelite:
        if satelites[next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((satelites[next_satelite-1].pos, satelites[next_satelite].pos))
            next_satelite = next_satelite + 1
        else:
            lines = []
            next_satelite = 0




#update function repeat it self 
def update():
    pass






create_satelite()

pgzrun.go()
