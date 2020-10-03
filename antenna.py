import pygame
pygame.init()

#Set window dimensions
displayWidth = 800
displayWeight = 800

#Initiate the window
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('MARS-Pitz - Antenna')
#Setting clock for game's time
clock = pygame.time.Clock()

antennaImg = pygame.image.load('antenna.png')

time = 0






def AntennaDisplay(x,y):
    gameDisplay.blit(antennaImg, (x,y))


# Starts the game
def GameLoop():

    x = (displayWidth * 0.7)
    y = (display_Height * 0.8)

    # Loop if the user doesn't close the game
    gameExit = False
    while not gameExit:

        # Finish the program if the user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    if (pygame.time.get_ticks):
                        time = pygame.time.get_ticks




                    if (pygame.time.Clock.get_time()/1000) == 4:
                        cool
                    tonto
                else:
                    print('tonto')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    time = pygame.time.Clock.tick


                    if time = 0:
                        start tick()

                    else:
                        if get_time < 4:
                            start tick()
                            se mueve la flecha
                        else:
                            pierdes





# Exit from the game window
game.quit()
quit()
