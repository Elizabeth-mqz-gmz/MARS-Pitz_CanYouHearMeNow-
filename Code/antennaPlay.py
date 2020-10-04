import pygame as pg
import random as rd
import time   as tm


#init and display
pg.init()

screen = pg.display.set_mode((600,600))
pg.display.set_caption("Marz-Pitz")

   
##intervalos
a1 = 0.5
a2 = 1.5
b1 = 2
b2 = 3
c1 = 4
c2 = 5

#level
l = rd.randint(0,2)

#images


sunImg = pg.image.load('../Media/Antenna/Orbits.png')
conImg = pg.image.load('../Media/Antenna/Console.png')
antImg = pg.image.load('../Media/Antenna/Antenna.png')
wndImg = pg.image.load('../Media/Antenna/Window.png')
walImg = pg.image.load('../Media/Antenna/Wall.png')
wvsImg = pg.image.load('../Media/Antenna/Waves.png')
srnImg = pg.image.load('../Media/Antenna/Screen.png')
prgImg = pg.image.load('../Media/Antenna/Paragraph.png')
cldImg = pg.image.load('../Media/Antenna/Cloud.png')
barImg = pg.image.load('../Media/Antenna/Bar.png')
winImg = pg.image.load('../Media/Antenna/Win.png')

sunImg = pg.transform.scale(sunImg, (500, 500))
conImg = pg.transform.scale(conImg, (500, 250))
antImg = pg.transform.scale(antImg, (300, 600))
wndImg = pg.transform.scale(wndImg, (300, 600))
walImg = pg.transform.scale(walImg, (300, 600))
wvsImg = pg.transform.scale(wvsImg, (531, 1062))
srnImg = pg.transform.scale(srnImg, (250, 500))
prgImg = pg.transform.scale(prgImg, (200, 270))
cldImg = pg.transform.scale(cldImg, (100, 100))
barImg = pg.transform.scale(barImg, (333, 625))
winImg = pg.transform.scale(winImg, (384, 96))


#background paint
screen.fill((160,255,244))

screen.blit(cldImg, (500,80))
screen.blit(cldImg, (300,120))
screen.blit(antImg, (300,100))
screen.blit(wndImg, (300,0))
screen.blit(walImg, (0,0))
screen.blit(conImg, (0,350))
screen.blit(srnImg, (0,0))
screen.blit(prgImg, (0,0))
screen.blit(sunImg, (0,380),(0,0,250,250))
screen.blit(barImg, (7,310),(0,0,333,41))



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
        if vel > a1 and vel <= a2:
            screen.blit(wvsImg, (390,0),(177,0,177,354))   
        elif vel > b1 and vel < a1:
            screen.blit(wvsImg, (390,0),(354,354,177,354))   
        else:    
            screen.blit(wvsImg, (390,0),(0,708,177,354))   
    elif lev == 1:
        if vel > b2:
            screen.blit(wvsImg, (390,0),(354,0,177,354))   
        elif vel > b1 and vel <= b2:
            screen.blit(wvsImg, (390,0),(0,354,177,354))   
        else:    
            screen.blit(wvsImg, (390,0),(0,708,177,354))   
    elif lev == 2:
        if vel > a1:
            screen.blit(wvsImg, (390,0),(354,0,177,354))   
        elif vel > b2 and vel <= a1:
            screen.blit(wvsImg, (390,0),(354,354,177,354))   
        elif vel > c1 and vel <= c2:    
            screen.blit(wvsImg, (390,0),(354,708,177,354))   


def barUpdate(level, sublevel):
    if level == 1:
        sublevel = sublevel + 5
    elif level == 2:
        sublevel = sublevel + 10

    fac = int(sublevel*41.6)

    screen.blit(barImg, (7,310),(0,fac,333,41))

#end
def win():
    for x in range(1,5):
        if x%2 == 0:
            screen.blit(winImg, (108,276),(0,0,384,48))
        else:
            screen.blit(winImg, (108,276),(0,48,384,48))
        pg.display.update()
        tm.sleep(1)
    #codigo de regreso a principal    


#play
playing = True

while playing:
    for events in pg.event.get():
        if events.type == pg.QUIT:
            win()
            playing = False

    #barUpdate(2,3)
    
    onda(6.3,0)

    pg.display.update()


quit()