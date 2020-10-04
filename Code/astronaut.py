import pygame as pg
import random

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

        max = 200
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
        return True


def printImage (image,x,y):
    gameDisplay.blit(image, (x,y))

def Final_Msg(points):
	pg.init()

	# define the RGB value for colors,
	white = (255, 255, 255)
	green = (0, 255, 0)
	blue = (0, 0, 128)
	black = (0, 0, 0)

	# assigning values to X and Y variable
	X = 700
	Y = 500
	display_surface = pg.display.set_mode((X, Y ))

	# set the pygame window name
	pg.display.set_caption('Show Text')

	# create a font object.
	font = pg.font.Font('freesansbold.ttf', 16)

	# create a text suface object, on which text is drawn on it.
	text = font.render('Good Job. You obtained ' + str(points) +' points. We encourage you to keep trying!', True, green, blue)

	# create a rectangular object for the text surface object
	textRect = text.get_rect()

	# set the center of the rectangular object.
	textRect.center = (X // 2, Y // 2)

	# infinite loop
	while True :
		display_surface.fill(black)

		# copying the text surface object to the display surface object  at the center coordinate.
		display_surface.blit(text, textRect)

		# iterate over the list of Event objects  that was returned by pygame.event.get() method.
		for event in pg.event.get():

			# if event object type is QUIT then quitting the pygame  and program both.
			if event.type == pg.QUIT:
				# deactivates the pygame library
				pg.quit()
				# quit the program.
				quit()
			# Draws the surface object to the screen.
			pg.display.update()

def gameLoop():

    astro = Astronaut("astronaut.png")
    # obs1 = Obstacle("obstacle1.png")
    no_objetos = 20
    obs_vec = []
    obs_vec.append(Obstacle("obstacle1.png",displayWidth,displayHeight - 50 ))

    points = 0
    # interference
    # The astronaut could receive the instructions with delay
    inter = 1

    change = False
    time = 1

    #Loop if the Astronaut doesn´t crash or the user doesn't close the game
    while not astro.crashed:

            for event in pg.event.get():

                #Finish the program if the user closes the window
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP and not astro.jumpping["isJummping"]:
                        pg.time.set_timer(pg.USEREVENT+2, 100*inter)

                if event.type == pg.USEREVENT+1:
                    # print(time)
                    if time > 3 and change:
                        inter = random.randrange(1, 5)
                        print(inter)
                        change = False
                    # Make random the time of creation of new obstacles
                    time = random.randrange(1,6)
                    pg.time.set_timer(pg.USEREVENT+1, 1000*time)
                    obs_vec.append(Obstacle("obstacle1.png",displayWidth,displayHeight - 50 ))

                if event.type == pg.USEREVENT+2:
                    pg.time.set_timer(pg.USEREVENT+2, 0)
                    astro.jumpping["isJummping"] = True
                    astro.jumpping["up"] = True

                if event.type == pg.USEREVENT+3:
                    change = True

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
                    points += 1*inter
                    obs = obs_vec.pop(0)
                    del obs


            astro.jump()
            pg.display.flip()
    return points

# -------

displayWidth = 800
displayHeight = 600

#Initiate the window
gameDisplay = pg.display.set_mode((displayWidth, displayHeight))
pg.display.set_caption("MARS-Pitz - Astronaut")
clock = pg.time.Clock()

# Set an event to instance obstacles
pg.time.set_timer(pg.USEREVENT+1, 6000)

# Change the delay
pg.time.set_timer(pg.USEREVENT+3, 2000)

points = gameLoop()
# Exit from the game
Final_Msg(points)
pg.quit()
quit()
