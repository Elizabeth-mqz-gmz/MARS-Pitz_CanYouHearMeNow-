import pygame as pg
import sys
import os
import time
import Minigames.Antena
from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

        self.go_to_minigame = False
        self.on_minigame = False
        self.minigame_class = False

        self.game_folder = path.dirname(__file__)
        self.media_folder = path.join(self.game_folder, '..', 'Media')
        self.load_data()

    def load_data(self):

        self.map = TiledMap(path.join(self.media_folder, 'Base map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(self.media_folder, 'Base', PLAYER_IMG)).convert_alpha()
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0,0,0, 180))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mini_game = pg.sprite.Group()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'Player':
                self.player = Player(self, tile_object.x/TILESIZE, tile_object.y/TILESIZE)
            elif tile_object.type == 'MiniGame':
                MiniGame(self, tile_object.name, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            else:
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            if self.on_minigame and not self.go_to_minigame:
                self.quit_minigame()

            self.dt = self.clock.tick(FPS) / 1000.0
            if self.minigame_class:
                if(self.on_minigame):
                    self.on_minigame.tick()
                else:
                    self.on_minigame = self.minigame_class(self.quit_minigame, self)
            else:
                self.events()
                self.update()
                self.draw()

    def quit_minigame(self):
        self.go_to_minigame = False
        self.on_minigame = False
        self.minigame_class = False

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        if self.go_to_minigame:
            self.screen.blit(self.dim_screen, (0, 0))
            font = pg.font.SysFont('Arial', 20)
            text_surface = font.render("Press F to go to minigame "+self.go_to_minigame, True, LIGHTGREY)
            text_rect = text_surface.get_rect()
            text_rect.center = (WIDTH/2, HEIGHT/2)
            self.screen.blit(text_surface, text_rect)

        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()