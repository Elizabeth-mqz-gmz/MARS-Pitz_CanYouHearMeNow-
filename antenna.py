import pygame
pygame.init()

#Set window dimensions
displayWidth = 800
displayHeight = 800

#Initiate the window
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('MARS-Pitz - Antenna')


# antennaImg = pygame.image.load('antenna.png')
bandera = False

def AntennaDisplay(x,y):
    gameDisplay.blit(antennaImg, (x,y))


# Starts the game
def GameLoop(bandera):

    x = (displayWidth * 0.7)
    y = (displayHeight * 0.8)

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

                    if bandera:
                        clock.tick()
                        print ("Se reinicio el tiempo")


                    else:
                        #Setting clock for game's time
                        print ("El origen")
                        clock = pygame.time.Clock()
                        clock.tick()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    #time = pygame.time.Clock.tick

                    if bandera:
                        time = clock.get_time()/1000

                        if time > 3:
                            #bandera = False
                            print ("Mal hecho")

                        else:
                            #x_change = 5
                            print ("Bien hecho")
                            clock.tick()

                    else:
                        bandera = True

# Starts
GameLoop(bandera)

# Exit from the game window
game.quit()
quit()
