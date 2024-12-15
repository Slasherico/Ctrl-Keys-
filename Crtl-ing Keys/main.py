import pygame
from time import sleep

from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        self.player_x = 200
        self.player_y = 200
        self.keys = [False, False, False, False]
        self.running = True
        self.player = pygame.image.load("images/rocket.png")
        self.background = pygame.image.load("images/space_bckgrnd.png")
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    self.keys[0] = True
                elif event.key == K_DOWN:
                    self.keys[1] = True
                elif event.key == K_LEFT:
                    self.keys[2] = True
                elif event.key == K_RIGHT:
                    self.keys[3] = True
            if event.type == pygame.KEYUP:
                if event.key == K_UP:
                    self.keys[0] = False
                if event.key == K_DOWN:
                    self.keys[1] = False
                if event.key == K_LEFT:
                    self.keys[2] = False
                if event.key == K_RIGHT:
                    self.keys[3] = False
    def player_pos(self):
        if self.keys[0] and self.player_y > 0:
            self.player_y -= 15
        if self.keys[1] and self.player_y < 600:
            self.player_y += 15
        if self.keys[2] and self.player_x > 0:
            self.player_x -= 15
        if self.keys[3] and self.player_x < 600:
            self.player_x += 15
        self.player_y += 5
            
    def display(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.player, (self.player_x, self.player_y))
        pygame.display.flip()
    def run(self):
        while self.running and self.player_y < 600:
            self.handle_events()
            self.player_pos()
            self.display()
            sleep(0.05)
        pygame.QUIT()
if __name__ == '__main__':
    game = Game()
    game.run()