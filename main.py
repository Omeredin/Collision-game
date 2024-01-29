import pygame
import sys
import random
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()

        # Get the screen width and height
        screen_info = pygame.display.Info()
        self.screenWidth = screen_info.current_w
        self.screenHeight = screen_info.current_h

        # Set the window size to fullscreen
        self.windowSurface = pygame.display.set_mode((self.screenWidth, self.screenHeight), FULLSCREEN, 32)

        pygame.display.set_caption('Collision Detection')

        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.WHITE = (255, 255, 255)

        self.foodCounter = 0
        self.NEWFOOD = 40
        self.FOODSIZE = 20
        self.player = pygame.Rect(300, 100, 50, 50)
        self.foods = []

        for i in range(20):
            self.foods.append(pygame.Rect(random.randint(0, self.screenWidth - self.FOODSIZE),
                                           random.randint(0, self.screenHeight - self.FOODSIZE),
                                           self.FOODSIZE, self.FOODSIZE))

        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        self.MOVESPEED = 6

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    self.moveRight = False
                    self.moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    self.moveRight = True
                    self.moveLeft = False
                if event.key == K_UP or event.key == K_w:
                    self.moveUp = True
                    self.moveDown = False
                if event.key == K_DOWN or event.key == K_s:
                    self.moveUp = False
                    self.moveDown = True
                if event.key == K_x:
                    self.player.top = random.randint(0, self.screenHeight - self.player.height)
                    self.player.left = random.randint(0, self.screenWidth - self.player.width)
            if event.type == MOUSEBUTTONUP:
                self.foods.append(pygame.Rect(event.pos[0], event.pos[1], self.FOODSIZE, self.FOODSIZE))

    def update(self):
        self.foodCounter += 1
        if self.foodCounter >= self.NEWFOOD:
            self.foodCounter = 0
            self.foods.append(pygame.Rect(random.randint(0, self.screenWidth - self.FOODSIZE),
                                           random.randint(0, self.screenHeight - self.FOODSIZE),
                                           self.FOODSIZE, self.FOODSIZE))

        self.windowSurface.fill(self.WHITE)
        if self.moveDown and self.player.bottom < self.screenHeight:
            self.player.top += self.MOVESPEED
        if self.moveUp and self.player.top > 0:
            self.player.top -= self.MOVESPEED
        if self.moveLeft and self.player.left > 0:
            self.player.left -= self.MOVESPEED
        if self.moveRight and self.player.right < self.screenWidth:
            self.player.right += self.MOVESPEED

        pygame.draw.rect(self.windowSurface, self.BLACK, self.player)

        for food in self.foods:
            if self.player.colliderect(food):
                self.foods.remove(food)

        for i in range(len(self.foods)):
            pygame.draw.rect(self.windowSurface, self.GREEN, self.foods[i])

    def run(self):
        while True:
            self.handle_events()
            self.update()

            pygame.display.update()
            self.mainClock.tick(40)

if __name__ == "__main__":
    game = Game()
    game.run()

