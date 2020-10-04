import pygame as pg
import time as tm


class Antena:
    def __init__(self, quit, game):
        self.quit = quit
        self.game = game
        self.screen = game.screen
        self.limits = [5, 7, 2, 4, 0, 1]
        pg.display.set_caption('MARS-Pitz - Antenna')
        self.run()

    def run(self):
        self.load_data()

    def load_data(self):
        # Load the images & graphics
        self.sunImg = pg.image.load('./Media/Antenna/Orbits.png')
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
        self.sunImg = pg.transform.scale(sunImg, (500, 500))
        self.conImg = pg.transform.scale(conImg, (500, 250))
        self.antImg = pg.transform.scale(antImg, (300, 600))
        self.wndImg = pg.transform.scale(wndImg, (300, 600))
        self.walImg = pg.transform.scale(walImg, (300, 600))
        self.wvsImg = pg.transform.scale(wvsImg, (531, 1062))
        self.srnImg = pg.transform.scale(srnImg, (360, 500))
        self.prgImg = pg.transform.scale(prgImg, (300, 270))
        self.cldImg = pg.transform.scale(cldImg, (100, 100))
        self.barImg = pg.transform.scale(barImg, (333, 665))
        self.winImg = pg.transform.scale(winImg, (384, 96))
        self.lseImg = pg.transform.scale(lseImg, (384, 96))

    def draw(self, level, sublevel, limits, vel, fg):
        # Paint the background
        self.screen.fill((160, 255, 244))

        # Display the some images
        self.screen.blit(cldImg, (500, 80))
        self.screen.blit(cldImg, (300, 120))
        self.screen.blit(antImg, (300, 100))
        self.screen.blit(wndImg, (300, 0))
        self.screen.blit(walImg, (0, 0))
        self.screen.blit(conImg, (0, 350))
        self.screen.blit(srnImg, (0, 0))
        self.screen.blit(prgImg, (0, 0))
        self.screen.blit(sunImg, (0, 380), (0, 0, 250, 250))
        self.screen.blit(barImg, (7, 310), (0, 0, 333, 41))

        check = True
        SelectLevel(level, sublevel)

        if vel != 0:
            if fg:
                check = Waves(vel, level - 1, limits)
            else:
                check = Waves(vel, level, limits)
        pg.display.update()
        return check

    def win(self):
        for x in [1, 2, 3, 4, 5]:
            if x % 2 == 0:
                self.screen.blit(winImg, (108, 276), (0, 0, 384, 48))
            else:
                self.screen.blit(winImg, (108, 276), (0, 48, 384, 48))
            pg.display.update()
            tm.sleep(1)

    def lose(self):
        for x in [1, 2, 3, 4, 5]:
            if x % 2 == 0:
                self.screen.blit(lseImg, (108, 276), (0, 0, 384, 48))
            else:
                self.screen.blit(lseImg, (108, 276), (0, 48, 384, 48))
            pg.display.update()
            tm.sleep(1)

    def barUpdate(level, sublevel):
        print(level, sublevel)
        if level == 1:
            sublevel += 5
        elif level == 2:
            sublevel += 10
        fac = int(sublevel * 41.6)
        self.screen.blit(barImg, (7, 310), (0, fac, 333, 41))
        pg.display.update()

    # Display the specific image pattern of each level, and return the level's range
    def SelectLevel(self, l, sl):
        # print(l,sl)

        if l == 0:
            self.screen.blit(sunImg, (0, 380), (0, 250, 250, 250))
            self.screen.blit(wvsImg, (390, 0), (0, 0, 177, 354))
        elif l == 1:
            self.screen.blit(sunImg, (0, 380), (250, 0, 250, 250))
            self.screen.blit(wvsImg, (390, 0), (177, 354, 177, 354))
        elif l == 2:
            self.screen.blit(sunImg, (0, 380), (250, 250, 250, 250))
            self.screen.blit(wvsImg, (390, 0), (177, 708, 177, 354))

    # Display the waves effect of each space event
    def Waves(vel, lev, limits):
        rt = False
        if lev == 0:
            if limits[0] < vel <= limits[1]:
                screen.blit(wvsImg, (390, 0), (177, 0, 177, 354))
                rt = True
            elif limits[2] < vel < limits[0]:
                screen.blit(wvsImg, (390, 0), (354, 354, 177, 354))
            elif vel < limits[2]:
                screen.blit(wvsImg, (390, 0), (0, 708, 177, 354))
        elif lev == 1:
            if vel > limits[3]:
                screen.blit(wvsImg, (390, 0), (354, 0, 177, 354))
            elif limits[2] < vel <= limits[3]:
                screen.blit(wvsImg, (390, 0), (0, 354, 177, 354))
                rt = True
            elif vel < limits[2]:
                screen.blit(wvsImg, (390, 0), (0, 708, 177, 354))
        elif lev == 2:
            if vel > limits[0]:
                screen.blit(wvsImg, (390, 0), (354, 0, 177, 354))
            elif limits[5] < vel <= limits[0]:
                screen.blit(wvsImg, (390, 0), (354, 354, 177, 354))
            elif limits[4] < vel <= limits[5]:
                screen.blit(wvsImg, (390, 0), (354, 708, 177, 354))
                rt = True
        return rt

    def tick(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                self.game.quit()

            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                if self.startedGame:
                    self.clock.tick()

                else:
                    self.clock = pg.time.Clock()
                    self.clock.tick()

            if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                if self.startedGame:

                    self.time = clock.get_time() / 1000

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

                    if Draw(self.counterLevel, self.counterSubLevel, self.limits, self.time, self.flag):
                        self.clock.tick()
                        BarUpdate(self.counterLevel, self.counterSubLevel)
                    else:
                        self.lose = True
                        tm.sleep(1)
                        self.lose()
                else:
                    self.startedGame = True
