import pygame as pg
import random
from os import path


class Signal:
    def __init__(self, image, x, y, media_folder, gameDisplay):
        self.image = pg.image.load(path.join(media_folder, 'Astronaut', image))
        self.image = pg.transform.scale(self.image, (100, 100))
        self.coord = [x, y]
        self.level = 1
        self.gameDisplay = gameDisplay

    def change(self):
        coords = [[0, self.image.get_height() / 2], [self.image.get_width() / 2, 0],
                  [0, 0], [self.image.get_width() / 2, self.image.get_height() / 2]]
        # printImage(self.image, self.coord[0], self.coord[1])
        self.gameDisplay.blit(self.image, (self.coord[0], self.coord[1]), (
            coords[self.level - 1][0], coords[self.level - 1][1], self.image.get_width() / 2,
            self.image.get_height() / 2))


class Astronaut:
    def __init__(self, image, media_folder, gameDisplay):
        self.image = pg.image.load(path.join(media_folder, 'Astronaut', image))
        self.coord = [0, displayHeight - self.image.get_height()]
        self.crashed = False
        self.foot = (self.image.get_width() / 12 - 20, self.image.get_width() / 12 + 20)
        self.head = (self.image.get_width() / 12 - 20, self.image.get_width() / 12 + 20)
        self.jumpping = {"isJummping": False,
                         "up": False}
        self.gameDisplay = gameDisplay
        self.sprite = 0

    def jump(self):

        # The astronaut will only jump every time he
        # finishes a jump cycle, this means
        # that he must go up and down to do it again

        max = displayHeight - self.image.get_height() - 100
        min = displayHeight - self.image.get_height()
        increment = 3

        if self.jumpping["isJummping"]:
            if self.coord[1] > max and self.jumpping["up"]:
                self.coord[1] -= increment
                if self.coord[1] <= max:
                    self.jumpping["up"] = False

            elif self.coord[1] < min and not self.jumpping["up"]:
                self.coord[1] += 2
                if self.coord[1] >= min:
                    self.jumpping["up"] = True
                    self.jumpping["isJummping"] = False
        else:
            self.move()
        width = self.image.get_width() / 6
        self.gameDisplay.blit(self.image, (self.coord[0], self.coord[1]),
                              (width * self.sprite, 0, width, self.image.get_height()))

    # Animate astronaut running
    def move(self):
        if self.sprite < 5:
            self.sprite += 1
        else:
            self.sprite = 0


class Obstacle:
    def __init__(self, image, x, y, media_folder, gameDisplay):
        self.image = pg.image.load(path.join(media_folder, 'Astronaut', image))
        self.image = pg.transform.scale(self.image, (78, 56))
        self.gameDisplay = gameDisplay
        self.coord = [x, y]
        self.pas = False

    def move(self, vel):
        if self.image.get_width() + self.coord[0] > 0:
            self.coord[0] -= vel
            self.gameDisplay.blit(self.image, (self.coord[0], self.coord[1]))
        # The atronaut pased the obstacle
        else:
            self.pas = True


def check(astro, obs, up):
    if astro.image.get_height() + astro.coord[1] >= obs.coord[1] and up == False:
        return True
    if astro.coord[1] <= obs.coord[1] + obs.image.get_height() and up == True:
        return True


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
    display_surface = pg.display.set_mode((X, Y))

    # set the pygame window name
    pg.display.set_caption('Show Text')

    # create a font object.
    font = pg.font.Font('freesansbold.ttf', 16)

    # create a text suface object, on which text is drawn on it.
    text = font.render('Good Job. You obtained ' + str(points) + ' points. We encourage you to keep trying!', True,
                       green, blue)

    # create a rectangular object for the text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)

    start = pg.time.get_ticks()
    now = pg.time.get_ticks
    # infinite loop
    while now() - start <= 2000:
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


pg.display.set_caption("Mars-Pitz - Astronaut")
clock = pg.time.Clock()
displayWidth = 800
displayHeight = 600


class AstronautGame:
    def __init__(self, quit, game):
        self.quit = quit
        self.game = game
        self.gameDisplay = pg.display.set_mode((displayWidth, displayHeight))
        self.media_folder = game.media_folder

        self.start()

    def tick(self):
        pass

    def start(self):
        # Set an event to instance obstacles
        pg.time.set_timer(pg.USEREVENT + 1, 6000)

        # Change the delay
        pg.time.set_timer(pg.USEREVENT + 3, 1000)

        # Set an event to instance obstacles (up)
        pg.time.set_timer(pg.USEREVENT + 4, 4000)

        points = self.gameLoop()
        # Exit from the game with a message saying your points.
        Final_Msg(points)

        pg.display.set_mode((600, 600))
        self.quit()

    def gameLoop(self):
        # set
        hand = pg.image.load(path.join(self.media_folder, 'Astronaut', 'Hand.png'))
        hand = pg.transform.scale(hand, (448, 224))

        back = pg.image.load(path.join(self.media_folder, 'Astronaut', 'Background.png'))
        back = pg.transform.scale(back, (800, 200))

        astro = Astronaut("Run.png", self.media_folder, self.gameDisplay)

        obs_vec, obs_vec_up = [], []
        # obs_vec.append(Obstacle("Obstacle1.png", displayWidth, displayHeight - 56, self.media_folder, self.gameDisplay))
        # obs_vec_up.append(Obstacle("Obstacle1.png", displayWidth - 70, displayHeight - 350, self.media_folder, self.gameDisplay))

        points = 0
        # interference
        # The astronaut could receive the instructions with delay
        signal = Signal("Signal.png", 90, 70, self.media_folder, self.gameDisplay)

        change = False
        time = 1

        # Loop if the Astronaut doesn´t crash or the user doesn't close the game
        while not astro.crashed:

            for event in pg.event.get():

                # Finish the program if the user closes the window
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP and not astro.jumpping["isJummping"]:
                        pg.time.set_timer(pg.USEREVENT + 2, 100 * signal.level)

                if event.type == pg.USEREVENT + 1:
                    # print(time)
                    if time > 3 and change:
                        signal.level = random.randrange(1, 4)
                        change = False
                        print(signal.level)
                    # Make random the time of creation of new obstacles
                    time = random.randrange(2, 6)
                    pg.time.set_timer(pg.USEREVENT + 1, 1000 * time)
                    obs_vec.append(
                        Obstacle("Obstacle{}.png".format(random.randrange(1, 7)), displayWidth, displayHeight - 56,
                                 self.media_folder, self.gameDisplay))

                if event.type == pg.USEREVENT + 2:
                    pg.time.set_timer(pg.USEREVENT + 2, 0)
                    astro.jumpping["isJummping"] = True
                    astro.jumpping["up"] = True

                if event.type == pg.USEREVENT + 3:
                    change = True

                if event.type == pg.USEREVENT + 4:
                    obs_vec_up.append(
                        Obstacle("Obstacle{}.png".format(random.randrange(1, 6)), displayWidth, displayHeight - 350,
                                 self.media_folder, self.gameDisplay))

            self.gameDisplay.fill((0, 0, 0))

            if len(obs_vec):
                if astro.foot[1] >= obs_vec[0].coord[0] >= astro.foot[0]:
                    astro.crashed = check(astro, obs_vec[0], False)

            if len(obs_vec_up):
                if astro.head[1] >= obs_vec_up[0].coord[0] >= astro.head[0]:
                    astro.crashed = check(astro, obs_vec_up[0], True)

            self.gameDisplay.blit(hand, (0, 0))
            self.gameDisplay.blit(back, (0, displayHeight - back.get_height()))
            # Ground objects
            i = 0
            while i < len(obs_vec):
                if not obs_vec[i].pas:
                    obs_vec[i].move(3)
                    i += 1
                else:
                    points += 1 * signal.level
                    obs = obs_vec.pop(0)
                    del obs
            # Head Objects
            i = 0
            while i < len(obs_vec_up):
                if not obs_vec_up[i].pas:
                    obs_vec_up[i].move(3)
                    i += 1
                else:
                    points += 1 * signal.level
                    obs = obs_vec_up.pop(0)
                    del obs

            astro.jump()
            signal.change()
            pg.display.flip()
        return points

    def printImage(self, image, x, y):
        self.gameDisplay.blit(image, (x, y))
