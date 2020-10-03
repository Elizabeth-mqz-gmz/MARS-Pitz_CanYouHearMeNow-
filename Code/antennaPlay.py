import pygame as pg
import random as rd
from textwrap import fill


#init and display
pg.init()

screen = pg.display.set_mode((600,600))
pg.display.set_caption("Marz-Pitz")

   
#level
l = rd.randint(0,2)

#images

sunImg = pg.image.load('../Media/Antenna/Orbits.png')
conImg = pg.image.load('../Media/Antenna/Console.png')
antImg = pg.image.load('../Media/Antenna/Antenna.png')
wndImg = pg.image.load('../Media/Antenna/Window.png')
walImg = pg.image.load('../Media/Antenna/Wall.png')
wvsImg = pg.image.load('../Media/Antenna/Waves.png')

sunImg = pg.transform.scale(sunImg, (500, 500))
conImg = pg.transform.scale(conImg, (500, 250))
antImg = pg.transform.scale(antImg, (300, 600))
wndImg = pg.transform.scale(wndImg, (300, 600))
walImg = pg.transform.scale(walImg, (300, 600))
wvsImg = pg.transform.scale(wvsImg, (531, 1062))



#background paint
screen.fill((160,255,244))

screen.blit(antImg, (300,100))
screen.blit(wndImg, (300,0))
screen.blit(walImg, (0,0))
screen.blit(conImg, (0,350))
screen.blit(sunImg, (0,380),(0,0,250,250))



pgp = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sit amet augue sed ligula faucibus dictum eu quis purus. Etiam ac dui magna. Phasellus eleifend, enim et ullamcorper pharetra, sapien diam faucibus massa, at laoreet nulla magna ut arcu. Mauris sodales quis mi eu scelerisque.\n Vestibulum sed malesuada sapien. Donec ut pulvinar lectus. Vivamus volutpat, augue quis lobortis maximus, sapien dui varius diam, vel scelerisque tellus sapien lacinia nisl. Donec.'
pgpf = fill(pgp, 50)

pg.font.init()
label = pg.font.SysFont('Sans Roman', 20)
txt = label.render(pgpf, False, (0, 0, 0))
#screen.blit(txt,(0,0),(0,0,200,500))

#test
v=0
l=0
#display the level
if l == 0:
    screen.blit(sunImg, (0,380),(250,250,250,250))   
    screen.blit(wvsImg, (390,0),(0,0,177,354))   
elif l == 1: 
    screen.blit(sunImg, (0,380),(0,250,250,250))  
    screen.blit(wvsImg, (390,0),(177,354,177,354))     
else:
    screen.blit(sunImg, (0,380),(250,0,250,250))  
    screen.blit(wvsImg, (390,0),(177,708,177,354)) 





pg.display.update()


def onda(vel,lev):
    if lev == 0:
        if vel == 0:
            screen.blit(wvsImg, (390,0),(177,0,177,354))   
        elif vel == 1:
            screen.blit(wvsImg, (390,0),(354,354,177,354))   
        elif vel == 2:    
            screen.blit(wvsImg, (390,0),(0,708,177,354))   
    elif lev == 1:
        if vel == 0:
            screen.blit(wvsImg, (390,0),(354,0,177,354))   
        elif vel == 1:
            screen.blit(wvsImg, (390,0),(0,354,177,354))   
        elif vel == 2:    
            screen.blit(wvsImg, (390,0),(0,708,177,354))   
    elif lev == 2:
        if vel == 0:
            screen.blit(wvsImg, (390,0),(354,0,177,354))   
        elif vel == 1:
            screen.blit(wvsImg, (390,0),(354,354,177,354))   
        elif vel ==2:    
            screen.blit(wvsImg, (390,0),(354,708,177,354))   



#play
playing = True

while playing:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            playing = False

    #v = funcionEliChava()
    
    onda(v,l)

    pg.display.update()


quit()