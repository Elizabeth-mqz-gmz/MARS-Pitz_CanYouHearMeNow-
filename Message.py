import pygame as pg
import random as rd
import time as tm

#Words
abc   = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letter= [pg.K_a,pg.K_b,pg.K_c,pg.K_d,pg.K_e,pg.K_f,pg.K_g,pg.K_h,pg.K_i,pg.K_j,pg.K_k,pg.K_l,pg.K_m,pg.K_n,pg.K_o,pg.K_p,pg.K_q,pg.K_r,pg.K_s,pg.K_t,pg.K_u,pg.K_v,pg.K_w,pg.K_x,pg.K_y,pg.K_z]
words = [ "MARS", "EARTH", "SPACE", "NASA", "STAR", "SPACESHIP", "HUMAN", "MARTIAN", "PLANET", "LIVE", "WATER", "OXYGEN", "FOOD"]
index = [None] * 16


winImg = pg.image.load('./Media/Message/Win.png')
lseImg = pg.image.load('./Media/Message/Lose.png')

winImg = pg.transform.scale(winImg, (384, 96))
lseImg = pg.transform.scale(lseImg, (384, 96))


#Cifrate a word
def Cifr():
    w = words[rd.randint(0,len(words)-1)]
    cont = 0
    for l in w:
        if l not in index:
            index[cont] = l
            cont += 1
    for i in index:
        while cont < len(index):
            val = abc[rd.randint(0,len(abc)-1)]
            if val not in index:
                index[cont] = val
                cont += 1

    rd.shuffle(index)
    return list(w)

#init and display
pg.init()

screen = pg.display.set_mode((600,600))
pg.display.set_caption("Marz-Pitz")

def text_objects(text,font):
    return font.render(text,True, (255,255,255))

def putLetter(leter,x,y):
    txt = pg.font.Font('freesansbold.ttf',20)
    TxtSur = text_objects(leter,txt)
    screen.blit(TxtSur,(x,y))

def win():
    for x in [1, 2, 3, 4, 5]:
        if x % 2 == 0:
            screen.blit(winImg, (108, 276), (0, 0, 384, 48))
        else:
            screen.blit(winImg, (108, 276), (0, 48, 384, 48))
        pg.display.update()
        tm.sleep(1)

def lose():
    for x in [1, 2, 3, 4, 5]:
        if x % 2 == 0:
            screen.blit(lseImg, (108, 276), (0, 0, 384, 48))
        else:
            screen.blit(lseImg, (108, 276), (0, 48, 384, 48))
        pg.display.update()
        tm.sleep(1)
#putLetter("ABC",10,30)

playing = True
while playing:
    errCount = 0
    pal = Cifr()
    loser = False
    print(pal)
    missing = len(pal)
    screen.fill((0,0,0))
    while (not loser) and playing:
        for events in pg.event.get():
            if events.type == pg.QUIT:
                playing = False
            elif events.type == pg.KEYDOWN:
                for lt in range(0,len(letter)-1):
                    if events.key == letter[lt]:
                        print(abc[lt])
                        if abc[lt] in pal:
                            pos = pal.index(abc[lt])
                            pal[pos] = " "
                            putLetter(abc[lt],30*(pos+2),30)
                            missing -= 1
                        else:
                            errCount += 1
                            putLetter("X",30*(errCount+2),90)
                        if missing == 0:
                            win()
                        if errCount == 3:
                            lose()
                            loser = True
        pg.display.update()


quit()
