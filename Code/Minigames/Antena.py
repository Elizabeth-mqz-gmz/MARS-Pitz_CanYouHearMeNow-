import pygame as pg
import time as tm
from os import path

class Antena:
    def __init__(self, quit, game):
        self.quit = quit
        self.game = game
        self.screen = game.screen
        self.limits = [5, 7, 2, 4, 0, 1]
        pg.display.set_caption('Mars Odyssey - Antenna')
        self.run()
        self.clock = pg.time.Clock()
        self.clock.tick()

    def run(self):
        self.load_data()
        self.draw(0, 0, self.limits, 0, False)
        self.counterLevel = 0
        self.counterSubLevel = 0
        self.time = 0
        self.startedGame = False
        self.lost = False
        self.gameExit = False

    def load_data(self):
        # Load the images & graphics
        self.sunImg = pg.image.load(path.join(self.game.media_folder, 'Antenna', 'Orbits.png'))
        self.conImg = pg.image.load('./Media/Antenna/Console.png')
        self.antImg = pg.image.load('./Media/Antenna/Antenna.png')
        self.wndImg = pg.image.load('./Media/Antenna/Window.png')
        self.walImg = pg.image.load('./Media/Antenna/Wall.png')
        self.wvsImg = pg.image.load('./Media/Antenna/Waves.png')
        self.srnImg = pg.image.load('./Media/Antenna/Screen.png')
        self.prgImg = pg.image.load('./Media/Antenna/Paragraph.png')
        self.cldImg = pg.image.load('./Media/Antenna/Cloud.png')
        self.barImg = pg.image.load('./Media/Antenna/Bar.png')
        self.winImg = pg.image.load('./Media/Antenna/Win.png')
        self.lseImg = pg.image.load('./Media/Antenna/Lose.png')

        # Resize the images
        self.sunImg = pg.transform.scale(self.sunImg, (500, 500))
        self.conImg = pg.transform.scale(self.conImg, (500, 250))
        self.antImg = pg.transform.scale(self.antImg, (300, 600))
        self.wndImg = pg.transform.scale(self.wndImg, (300, 600))
        self.walImg = pg.transform.scale(self.walImg, (300, 600))
        self.wvsImg = pg.transform.scale(self.wvsImg, (531, 1062))
        self.srnImg = pg.transform.scale(self.srnImg, (360, 500))
        self.prgImg = pg.transform.scale(self.prgImg, (300, 270))
        self.cldImg = pg.transform.scale(self.cldImg, (100, 100))
        self.barImg = pg.transform.scale(self.barImg, (333, 665))
        self.winImg = pg.transform.scale(self.winImg, (384, 96))
        self.lseImg = pg.transform.scale(self.lseImg, (384, 96))

    def draw(self, level, sublevel, limits, vel, fg):
        # Paint the background
        self.screen.fill((160, 255, 244))

        # Display the some images
        self.screen.blit(self.cldImg, (500, 80))
        self.screen.blit(self.cldImg, (300, 120))
        self.screen.blit(self.antImg, (300, 100))
        self.screen.blit(self.wndImg, (300, 0))
        self.screen.blit(self.walImg, (0, 0))
        self.screen.blit(self.conImg, (0, 350))
        self.screen.blit(self.srnImg, (0, 0))
        self.screen.blit(self.prgImg, (0, 0))
        self.screen.blit(self.sunImg, (0, 380), (0, 0, 250, 250))
        self.screen.blit(self.barImg, (7, 310), (0, 0, 333, 41))

        check = True
        self.selectLevel(level, sublevel)

        if vel != 0:
            if fg:
                check = self.waves(vel, level - 1, limits)
            else:
                check = self.waves(vel, level, limits)
        pg.display.flip()
        return check

    def win(self):
        for x in [1, 2, 3, 4, 5]:
            if x % 2 == 0:
                self.screen.blit(self.winImg, (108, 276), (0, 0, 384, 48))
            else:
                self.screen.blit(self.winImg, (108, 276), (0, 48, 384, 48))
            pg.display.update()
            tm.sleep(1)
            self.quit()

    def lose(self):
        for x in [1, 2, 3, 4, 5]:
            if x % 2 == 0:
                self.screen.blit(self.lseImg, (108, 276), (0, 0, 384, 48))
            else:
                self.screen.blit(self.lseImg, (108, 276), (0, 48, 384, 48))
            pg.display.update()
            tm.sleep(1)
            self.quit()

    def barUpdate(self, level, sublevel):
        print(level, sublevel)
        if level == 1:
            sublevel += 5
        elif level == 2:
            sublevel += 10
        fac = int(sublevel * 41.6)
        self.screen.blit(self.barImg, (7, 310), (0, fac, 333, 41))
        pg.display.update()

    # Display the specific image pattern of each level, and return the level's range
    def selectLevel(self, l, sl):
        # print(l,sl)

        if l == 0:
            self.screen.blit(self.sunImg, (0, 380), (0, 250, 250, 250))
            self.screen.blit(self.wvsImg, (390, 0), (0, 0, 177, 354))
        elif l == 1:
            self.screen.blit(self.sunImg, (0, 380), (250, 0, 250, 250))
            self.screen.blit(self.wvsImg, (390, 0), (177, 354, 177, 354))
        elif l == 2:
            self.screen.blit(self.sunImg, (0, 380), (250, 250, 250, 250))
            self.screen.blit(self.wvsImg, (390, 0), (177, 708, 177, 354))

    # Display the waves effect of each space event
    def waves(self, vel, lev, limits):
        rt = False
        if lev == 0:
            if limits[0] < vel <= limits[1]:
                self.screen.blit(self.wvsImg, (390, 0), (177, 0, 177, 354))
                rt = True
            elif limits[2] < vel < limits[0]:
                self.screen.blit(self.wvsImg, (390, 0), (354, 354, 177, 354))
            elif vel < limits[2]:
                self.screen.blit(self.wvsImg, (390, 0), (0, 708, 177, 354))
        elif lev == 1:
            if vel > limits[3]:
                self.screen.blit(self.wvsImg, (390, 0), (354, 0, 177, 354))
            elif limits[2] < vel <= limits[3]:
                self.screen.blit(self.wvsImg, (390, 0), (0, 354, 177, 354))
                rt = True
            elif vel < limits[2]:
                self.screen.blit(self.wvsImg, (390, 0), (0, 708, 177, 354))
        elif lev == 2:
            if vel > limits[0]:
                self.screen.blit(self.wvsImg, (390, 0), (354, 0, 177, 354))
            elif limits[5] < vel <= limits[0]:
                self.screen.blit(self.wvsImg, (390, 0), (354, 354, 177, 354))
            elif limits[4] < vel <= limits[5]:
                self.screen.blit(self.wvsImg, (390, 0), (354, 708, 177, 354))
                rt = True
        return rt

    def tick(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                self.game.quit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

                if event.key == pg.K_SPACE:
                    self.clock.tick()

            if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                if self.startedGame:

                    self.time = self.clock.get_time() / 1000

                    self.flag = False
                    if self.counterSubLevel == 4:
                        if self.counterLevel == 2:
                            self.gameExit = True
                            self.win()
                        self.counterSubLevel = 0
                        self.counterLevel += 1
                        self.flag = True

                    else:
                        self.counterSubLevel += 1

                    # print(flag, counterLevel,counterSubLevel)

                    if self.draw(self.counterLevel, self.counterSubLevel, self.limits, self.time, self.flag):
                        self.clock.tick()
                        self.barUpdate(self.counterLevel, self.counterSubLevel)
                    else:
                        self.lost = True
                        tm.sleep(1)
                        self.lose()
                else:
                    self.startedGame = True
