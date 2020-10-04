import pygame as pg
import time as tm

# Set the limits of each level's range
limits = [5, 7, 2, 4, 0, 1]

# Init and display
pg.init()

#Set window dimensions
displayWidth = 600
displayHeight = 600

#Initiate the window
screen = pg.display.set_mode((displayWidth, displayHeight))
pg.display.set_caption('MARS-Pitz - Antenna')

# Load the images & graphics
sunImg = pg.image.load('./Media/Antenna/Orbits.png')
conImg = pg.image.load('./Media/Antenna/Console.png')
antImg = pg.image.load('./Media/Antenna/Antenna.png')
wndImg = pg.image.load('./Media/Antenna/Window.png')
walImg = pg.image.load('./Media/Antenna/Wall.png')
wvsImg = pg.image.load('./Media/Antenna/Waves.png')
srnImg = pg.image.load('./Media/Antenna/Screen.png')
prgImg = pg.image.load('./Media/Antenna/Paragraph.png')
cldImg = pg.image.load('./Media/Antenna/Cloud.png')
barImg = pg.image.load('./Media/Antenna/Bar.png')
winImg = pg.image.load('./Media/Antenna/Win.png')
lseImg = pg.image.load('./Media/Antenna/Lose.png')

# Resize the images
sunImg = pg.transform.scale(sunImg, (500, 500))
conImg = pg.transform.scale(conImg, (500, 250))
antImg = pg.transform.scale(antImg, (300, 600))
wndImg = pg.transform.scale(wndImg, (300, 600))
walImg = pg.transform.scale(walImg, (300, 600))
wvsImg = pg.transform.scale(wvsImg, (531, 1062))
srnImg = pg.transform.scale(srnImg, (360, 500))
prgImg = pg.transform.scale(prgImg, (300, 270))
cldImg = pg.transform.scale(cldImg, (100, 100))
barImg = pg.transform.scale(barImg, (333, 665))
winImg = pg.transform.scale(winImg, (384, 96))
lseImg = pg.transform.scale(lseImg, (384, 96))

def Draw(level, sublevel, limits, vel, fg):
    # Paint the background
    screen.fill((160,255,244))

    # Display the some images
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

    check = True
    SelectLevel(level,sublevel)

    if vel != 0:
        if fg:
            check = Waves(vel, level-1, limits)
        else:
            check = Waves(vel, level, limits)
    pg.display.update()
    return check

#end
def Win():
    for x in [1,2,3,4,5]:
        if x%2 == 0:
            screen.blit(winImg, (108,276),(0,0,384,48))
        else:
            screen.blit(winImg, (108,276),(0,48,384,48))
        pg.display.update()
        tm.sleep(1)

def Lose():
    for x in [1,2,3,4,5]:
        if x%2 == 0:
            screen.blit(lseImg, (108,276),(0,0,384,48))
        else:
            screen.blit(lseImg, (108,276),(0,48,384,48))
        pg.display.update()
        tm.sleep(1)

def BarUpdate(level, sublevel):
    print(level,sublevel)
    if level == 1:
        sublevel += 5
    elif level == 2:
        sublevel += 10
    fac = int(sublevel*41.6)
    screen.blit(barImg, (7,310),(0,fac,333,41))
    pg.display.update()


# Display the specific image pattern of each level, and return the level's range
def SelectLevel(l,sl):
    #print(l,sl)
    

    if l == 0:
        screen.blit(sunImg, (0,380),(0,250,250,250))
        screen.blit(wvsImg, (390,0),(0,0,177,354))
    elif l == 1:
        screen.blit(sunImg, (0,380),(250,0,250,250))
        screen.blit(wvsImg, (390,0),(177,354,177,354))
    elif l == 2:
        screen.blit(sunImg, (0,380),(250,250,250,250))
        screen.blit(wvsImg, (390,0),(177,708,177,354))

# Display the waves effect of each space event
def Waves(vel,lev, limits):
    rt = False
    if lev == 0:
        if vel > limits[0] and vel <= limits[1]:
            screen.blit(wvsImg, (390,0),(177,0,177,354))
            rt = True
        elif vel > limits[2] and vel < limits[0]:
            screen.blit(wvsImg, (390,0),(354,354,177,354))
        elif vel < limits[2]:
            screen.blit(wvsImg, (390,0),(0,708,177,354))
    elif lev == 1:
        if vel > limits[3]:
            screen.blit(wvsImg, (390,0),(354,0,177,354))
        elif vel > limits[2] and vel <= limits[3]:
            screen.blit(wvsImg, (390,0),(0,354,177,354))
            rt = True
        elif vel < limits[2]:
            screen.blit(wvsImg, (390,0),(0,708,177,354))
    elif lev == 2:
        if vel > limits[0]:
            screen.blit(wvsImg, (390,0),(354,0,177,354))
        elif vel > limits[5] and vel <= limits[0]:
            screen.blit(wvsImg, (390,0),(354,354,177,354))
        elif vel > limits[4] and vel <= limits[5]:
            screen.blit(wvsImg, (390,0),(354,708,177,354))
            rt = True
    return rt

gameExit = False

while not gameExit:

    Draw(0, 0, limits, 0, False)
    counterLevel = 0
    counterSubLevel = 0
    time = 0
    startedGame = False
    lose = False
    
    while not lose:
        
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                quit()

            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                if startedGame:
                    clock.tick()

                else:
                    clock = pg.time.Clock()
                    clock.tick()
            
            if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                if startedGame:

                    time = clock.get_time()/1000

                    flag = False
                    if counterSubLevel == 4:
                        if counterLevel == 2:
                            gameExit = True
                            Win()
                        counterSubLevel = 0
                        counterLevel += 1
                        flag = True

                    else:
                        counterSubLevel += 1

                    #print(flag, counterLevel,counterSubLevel)

                    if Draw(counterLevel, counterSubLevel, limits, time, flag):
                        clock.tick
                        BarUpdate(counterLevel,counterSubLevel)
                    else:
                        lose = True
                        tm.sleep(1)
                        Lose()
                else:
                    startedGame = True


quit()