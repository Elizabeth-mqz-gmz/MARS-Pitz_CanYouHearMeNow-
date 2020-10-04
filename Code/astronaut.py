import pygame as pg

class Astronaut:
    def __init__(self,image):
        self.image = pg.image.load(image)
        self.coord = [0,displayHeight-self.image.get_height()]
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
    def __init__(self, image):
        self.image = pg.image.load(image)
        self.coord = [displayWidth,displayHeight-self.image.get_height()]
        self.passo = False

    def move(self, vel):
        if self.image.get_width() + self.coord[0] > 0:
            self.coord[0] -= vel
            printImage(self.image, self.coord[0],self.coord[1])

        #The atronaut passed the obstacle
        else:
            self.passo = True

def check(astro,obs):
    if astro.image.get_height() + astro.coord[1] >= obs.coord[1]:
        print("crash")
        return True


def printImage (image,x,y):
    gameDisplay.blit(image, (x,y))

def gameLoop():

    astro = Astronaut("astronaut.png")
    obs1 = Obstacle("obstacle1.png")
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
            if not obs1.passo:
                obs1.move(5)
            if obs1.coord[0] <= astro.image.get_width()-20:
                astro.crashed = check(astro, obs1)
            astro.jump()
            pg.display.flip()

displayWidth = 800
displayHeight = 600

#Initiate the window
gameDisplay = pg.display.set_mode((displayWidth, displayHeight))
pg.display.set_caption("MARS-Pitz - Astronaut")
clock = pg.time.Clock()

gameLoop()
# Exit from the game

game.quit()
quit()
