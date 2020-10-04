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

# Resize the images
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

def Draw(level, sublevel, limits, vel):
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

    SelectLevel(level)

    if vel != 0:
        Waves(vel, level, limits)

    BarUpdate(level, sublevel)

#end
def Win():
    for x in range(1,5):
        if x%2 == 0:
            screen.blit(winImg, (108,276),(0,0,384,48))
        else:
            screen.blit(winImg, (108,276),(0,48,384,48))
        pg.display.update()
        tm.sleep(1)

def BarUpdate(level, sublevel):

    if level == 1:
        sublevel += 5
    elif level == 2:
        sublevel += 10
    fac = int(sublevel*41.6)
    screen.blit(barImg, (7,310),(0,fac,333,41))

# Display the specific image pattern of each level, and return the level's range
def SelectLevel(level):
    if level == 0:
        screen.blit(sunImg, (0,380),(250,250,250,250))
        screen.blit(wvsImg, (390,0),(0,0,177,354))
        range = [limits[0], limits[1]]
    elif level == 1:
        screen.blit(sunImg, (0,380),(250,0,250,250))
        screen.blit(wvsImg, (390,0),(177,708,177,354))
        range = [limits[2],limits[3]]
    else:
        screen.blit(sunImg, (0,380),(0,250,250,250))
        screen.blit(wvsImg, (390,0),(177,354,177,354))
        range = [limits[4], limits[5]]
    pg.display.update()
    return range

# Display the waves effect of each space event
def Waves(vel,lev, limits):
    if lev == 0:
        if vel > limits[0] and vel <= limits[1]:
            screen.blit(wvsImg, (390,0),(177,0,177,354))
        elif vel > limits[2] and vel < limits[0]:
            screen.blit(wvsImg, (390,0),(354,354,177,354))
        else:
            screen.blit(wvsImg, (390,0),(0,708,177,354))
    elif lev == 1:
        if vel > limits[3]:
            screen.blit(wvsImg, (390,0),(354,0,177,354))
        elif vel > limits[2] and vel <= limits[3]:
            screen.blit(wvsImg, (390,0),(0,354,177,354))
        elif vel < limits[2]:
            screen.blit(wvsImg, (390,0),(0,708,177,354))
    elif lev == 2:
        if vel > limits[0]:
            screen.blit(wvsImg, (390,0),(354,0,177,354))
        elif vel > limits[5] and vel <= limits[0]:
            screen.blit(wvsImg, (390,0),(354,354,177,354))
        elif vel > limits[4] and vel <= limits[5]:
            screen.blit(wvsImg, (390,0),(354,708,177,354))

# All the game's mechanics are in this function
def GameLoop(startedGame):

    # Initialize the loop settings
    level = 0
    counterSubLevel = 0
    range = SelectLevel(level)

    # Loop if the user doesn't close the game
    gameExit = False
    while not gameExit:

        # Set new level and sub-level. Get new range
        if counterSubLevel == 5:
            level += 1
            counterSubLevel = 0
            range = SelectLevel(level)

        # Finish the program if the user closes the window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            # Check if the key "space" has been press
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:

                    # Restart the clock if it already exists
                    if startedGame:
                        clock.tick()

                    # Initialize a clock if it doesn't exist
                    else:
                        clock = pg.time.Clock()
                        clock.tick()

            # Get in when you stop pressing "space"
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:

                    # Calculate the time between the last "space" press
                    if startedGame:
                        time = clock.get_time()/1000

                        # Display a specific image pattern
                        Waves(time, level, limits)

                        # Check if the time between taps is correct
                        if (time < range[0]) or (time > range[1]):

                            #startedGame = False
                            level = 0
                            counterSubLevel = 0
                            # Show the level status in graphic way
                            Draw(level, counterSubLevel, limits, time)
                            #mostar linea vacia  (LOOOOOOOSEEEEER)


                        else:
                            clock.tick()
                            counterSubLevel += 1
                            # Show the level status in graphic way
                            Draw(level, counterSubLevel, limits, time)

                            # End the game when the user has finished the levels
                            if level == 2 and counterSubLevel == 4:
                                gameExit = True
                                #felicidades msj


                        pg.display.update()


                    else:
                        startedGame = True


# This flag helps in the first loop
startedGame = False

Draw(0, 0, limits, 0)
# Start the game
GameLoop(startedGame)
Win()


# Exits from the game's window
pg.quit()
quit()
