import pygame as pg
import utilities

class Astronaut:
    def __init__(self,image,x,y):
        self.image = image
        self.coord = [x,y]
        self.crashed = False
        self.jumpping = { "isJummping" : False,
                            "up" : False}

    def jump(self):

        #The astronaut will only jump every time he
        #finishes a jump cycle, this means
        #that he must go up and down to do it again

        max = 100
        min = 400
        increment = 3

        if self.jumpping["isJummping"]:
            if self.coord[1] > max and self.jumpping["up"]:
                self.coord[1] -= increment
                if self.coord[1] <= max:
                    self.jumpping["up"] = False

            elif self.coord[1] < min and not self.jumpping["up"]:
                self.coord[1] += increment
                if self.coord[1] >= min:
                    self.jumpping["up"] = True
                    self.jumpping["isJummping"] = False

        printImage(self.image, self.coord[0], self.coord[1])

class Obstacle:
    def __init__(self, image, x,y):
        self.image = image
        self.coord = [x,y]

    def move():
        

def check(Astronaut astronaut, Obstacle obstacle)



def printImage (image,x,y):
    gameDisplay.blit(image, (x,y))

def gameLoop():

    astro = Astronaut(pg.image.load("astronaut.png"), 0, 400)
    #Loop if the Astronaut doesn´t crash or the user doesn't close the game
    while not astro.crashed:

            for event in pg.event.get():

                #Finish the program if the user closes the window
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP and not astro.jumpping["isJummping"]:
                        astro.jumpping["isJummping"] = True
                        astro.jumpping["up"] = True

            gameDisplay.fill((0,0,0))
            astro.jump()
            pg.display.flip()

displayWidth = 800
displayHeight = 800

#Initiate the window
gameDisplay = pg.display.set_mode((displayWidth, displayHeight))
pg.display.set_caption("MARS-Pitz - Astronaut")
clock = pg.time.Clock()

gameLoop()
# Exit from the game
game.quit()
quit()
