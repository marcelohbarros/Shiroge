import pygame
from image import Image
import config as cfg

class Player:

    def __init__(self, x=0, y=0):
        self.sprite = Image("media/player.png", alpha=True)
        self.x = x
        self.y = y
        self.h = self.sprite.h / cfg.GAME_SCALE
        self.w = self.sprite.w / cfg.GAME_SCALE
        self.xSpeed = 0
        self.ySpeed = 0
        
        self.keysPressed = [False, False, False, False]
        self.UP = 0
        self.DOWN = 1
        self.LEFT = 2
        self.RIGHT = 3

        self.MAX_SPEED = 1

    def handleInputs(self, event):
        # Pressing key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not self.keysPressed[self.UP]:
                    self.ySpeed -= self.MAX_SPEED
                    self.keysPressed[self.UP] = True
            elif event.key == pygame.K_DOWN:
                if not self.keysPressed[self.DOWN]:
                    self.ySpeed += self.MAX_SPEED
                    self.keysPressed[self.DOWN] = True
            elif event.key == pygame.K_LEFT:
                if not self.keysPressed[self.LEFT]:
                    self.xSpeed -= self.MAX_SPEED
                    self.keysPressed[self.LEFT] = True
            elif event.key == pygame.K_RIGHT:
                if not self.keysPressed[self.RIGHT]:
                    self.xSpeed += self.MAX_SPEED
                    self.keysPressed[self.RIGHT] = True

        # Releasing key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if self.keysPressed[self.UP]:
                    self.ySpeed += self.MAX_SPEED
                    self.keysPressed[self.UP] = False
            elif event.key == pygame.K_DOWN:
                if self.keysPressed[self.DOWN]:
                    self.ySpeed -= self.MAX_SPEED
                    self.keysPressed[self.DOWN] = False
            elif event.key == pygame.K_LEFT:
                if self.keysPressed[self.LEFT]:
                    self.xSpeed += self.MAX_SPEED
                    self.keysPressed[self.LEFT] = False
            elif event.key == pygame.K_RIGHT:
                if self.keysPressed[self.RIGHT]:
                    self.xSpeed -= self.MAX_SPEED
                    self.keysPressed[self.RIGHT] = False

    def move(self):
        self.x += self.xSpeed
        
        # X out of bounds
        if self.x < 0:
            self.x = 0
        elif self.x + self.w > cfg.GAME_WIDTH:
            self.x = cfg.GAME_WIDTH - self.w

        self.y += self.ySpeed

        # Y out of bounds
        if self.y < 0:
            self.y = 0
        elif self.y + self.h > cfg.GAME_HEIGHT:
            self.y = cfg.GAME_HEIGHT - self.h

    def render(self, bufferSurface):
        self.sprite.render(bufferSurface, self.x, self.y)
