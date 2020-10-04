import pygame as pg
import random as rd


#init and display
pg.init()

screen = pg.display.set_mode((600,600))
pg.display.set_caption("Marz-Pitz")

def text_objects(text,font):
    return font.render(text,True, (255,255,255))

def putLetter(leter,i):
    txt = pg.font.Font('freesansbold.ttf',20)
    TxtSur = text_objects(leter,txt)
    screen.blit(TxtSur,(0,1))

putLetter("A",10)


playing = True
while playing:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            playing = False


    pg.display.update()


quit()