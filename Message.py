import pygame as pg
import pygame_textinput
import random as rd

#Words
abc   = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
words = [ "MARS", "EARTH", "SPACE", "NASA", "STAR", "SPACESHIP", "HUMAN", "MARTIAN", "PLANET", "LIVE", "WATER", "OXYGEN", "FOOD"]

#Cifrate a word
def Cifr():
    w = words[rd.randint(0,len(words)-1)]
    index = [None] * 16
    cont = 0
    for l in w:
        if l not in index:
            index[cont] = l
            cont += 1
    for i in index:
        while cont < len(index):
            val = abc[rd.randint(0,len(abc)-1)]
            if val not in index:
                index[cont] = val
                cont += 1

    rd.shuffle(index)
    print(index)
    return index

Cifr()

#init and display
pg.init()

screen = pg.display.set_mode((600,600))
pg.display.set_caption("Marz-Pitz")

def text_objects(text,font):
    return font.render(text,True, (255,255,255))

def putLetter(leter,x,y):
    txt = pg.font.Font('freesansbold.ttf',20)
    TxtSur = text_objects(leter,txt)
    screen.blit(TxtSur,(x,y))

putLetter("A",10,30)


textinput = pygame_textinput.TextInput()

playing = True
while playing:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            playing = False

     
    events = pg.event.get()
    textinput.update(events)
    screen.blit(textinput.get_surface(), (10, 10))
    pg.display.update()


quit()
