import pygame as pg

class Astronaut:
    def __init__(self,image):
        self.image = pg.image.load(image)
        self.coord = [0,displayHeight-self.image.get_height()]
        self.crashed = False
        self.foot = (self.image.get_width()/2 - 20, self.image.get_width()/2 + 20)
        self.jumpping = { "isJummping" : False,
                            "up" : False}

    def jump(self):

        #The astronaut will only jump every time he
        #finishes a jump cycle, this means
        #that he must go up and down to do it again

        max = 100
        min = displayHeight - self.image.get_height()
        increment = 1

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
    def __init__(self, image, x, y):
        self.image = pg.image.load(image)
        self.coord = [x,y]
        self.pas = False

    def move(self, vel):
        if self.image.get_width() + self.coord[0] > 0:
            self.coord[0] -= vel
            printImage(self.image, self.coord[0],self.coord[1])

        #The atronaut pased the obstacle
        else:
            self.pas = True

def check(astro,obs):
    if astro.image.get_height() + astro.coord[1] >= obs.coord[1]:
        print("crash")
        return True


def printImage (image,x,y):
    gameDisplay.blit(image, (x,y))

def gameLoop():

    astro = Astronaut("astronaut.png")
    # obs1 = Obstacle("obstacle1.png")
    no_objetos = 20
    obs_vec = []
    obs_vec.append(Obstacle("obstacle1.png",displayWidth,displayHeight - 50 ))

    #Loop if the Astronaut doesn´t crash or the user doesn't close the game
    points=0
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

                if event.type == pg.USEREVENT+1:
                    obs_vec.append(Obstacle("obstacle1.png",displayWidth,displayHeight - 50 ))

            gameDisplay.fill((0,0,0))

            if len(obs_vec):
                if obs_vec[0].coord[0] <= astro.foot[1] and obs_vec[0].coord[0] >= astro.foot[0]:
                    astro.crashed = check(astro, obs_vec[0])

            i = 0
            while i < len(obs_vec):
                if not obs_vec[i].pas:
                    obs_vec[i].move(2)
                    i += 1
                else:
                    points += 1
                    obs = obs_vec.pop(0)
                    del obs


            astro.jump()
            pg.display.flip()

displayWidth = 800
displayHeight = 600

#Initiate the window
gameDisplay = pg.display.set_mode((displayWidth, displayHeight))
pg.display.set_caption("MARS-Pitz - Astronaut")
clock = pg.time.Clock()

# evento = pygame.event.Event(pygame.USEREVENT, some_attr=1, other_attr='1')
pg.time.set_timer(pg.USEREVENT+1, 6000)

gameLoop()
# Exit from the game

pg.quit()
quit()
