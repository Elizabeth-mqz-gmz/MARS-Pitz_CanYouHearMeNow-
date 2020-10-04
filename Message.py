import pygame as pg
import random as rd

#Words
abc   = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
words = [ "MARS", "EARTH", "SPACE", "NASA", "STAR", "SPACESHIP", "HUMAN", "MARTIAN", "PLANET", "LIVE", "WATER", "OXYGEN", "FOOD"]

#Cifrate a word
def Cifr():
    w = words[rd.randint(0,len(words))]
    print(w)
    index = []
    for l in len(w):
        print(l)

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


playing = True
while playing:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            playing = False


    pg.display.update()


quit()