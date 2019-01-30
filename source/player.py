import pygame
from image import Image
from timer import Timer
import config as cfg

class Player:

    def __init__(self, x=0, y=0):
        self.sprite = Image("media/player.png", alpha=True)

        # Values from initial position are reused on player death
        self.xSpawn = x
        self.ySpawn = y - 0.1

        self.x = self.xSpawn
        self.y = self.ySpawn
        self.h = self.sprite.h / cfg.GAME_SCALE - 0.2
        self.w = self.sprite.w / cfg.GAME_SCALE
        self.xSpeed = 0
        self.ySpeed = 0

        self.timer = Timer()
        
        self.keysPressed = [False, False, False, False]
        self.UP = 0
        self.DOWN = 1
        self.LEFT = 2
        self.RIGHT = 3

        self.X_SPEED = 200
        self.JUMP_SPEED = 350
        self.GRAVITY = 600

        self.IN_GROUND = False
        self.DEAD = False

    def handleInputs(self, event):
        # Pressing key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not self.keysPressed[self.UP]:
                    self.keysPressed[self.UP] = True
                    if self.IN_GROUND:
                        self.ySpeed = -self.JUMP_SPEED
                        self.IN_GROUND = False
            elif event.key == pygame.K_LEFT:
                if not self.keysPressed[self.LEFT]:
                    self.xSpeed -= self.X_SPEED
                    self.keysPressed[self.LEFT] = True
            elif event.key == pygame.K_RIGHT:
                if not self.keysPressed[self.RIGHT]:
                    self.xSpeed += self.X_SPEED
                    self.keysPressed[self.RIGHT] = True

        # Releasing key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if self.keysPressed[self.UP]:
                    self.keysPressed[self.UP] = False
            if event.key == pygame.K_LEFT:
                if self.keysPressed[self.LEFT]:
                    self.xSpeed += self.X_SPEED
                    self.keysPressed[self.LEFT] = False
            elif event.key == pygame.K_RIGHT:
                if self.keysPressed[self.RIGHT]:
                    self.xSpeed -= self.X_SPEED
                    self.keysPressed[self.RIGHT] = False

    def __hasCollided(self, obj):
        if self.x > obj.x + obj.w:
            return False
        elif self.x + self.w < obj.x:
            return False
        elif self.y > obj.y + obj.h:
            return False
        elif self.y + self.h < obj.y:
            return False
        else:
            return True

    def move(self, wallList, spikeList):
        diff_time = self.timer.count()
        self.x += self.xSpeed * diff_time
        
        # X out of bounds
        if self.x < 0:
            self.x = 0
        elif self.x + self.w > cfg.GAME_WIDTH:
            self.x = cfg.GAME_WIDTH - self.w

        # Checks collision in X axis
        for wall in wallList:
            if self.__hasCollided(wall):
                # Collided from left
                if self.x < wall.x:
                    self.x = wall.x - self.w - 0.1
                # Collided from right
                else:
                    self.x = wall.x + wall.w + 0.1
        for spike in spikeList:
            if self.__hasCollided(spike):
                # Collided from left
                if self.x < spike.x:
                    self.x = spike.x - self.w - 0.1
                # Collided from right
                else:
                    self.x = spike.x + spike.w + 0.1

        self.y += self.ySpeed * diff_time
        self.ySpeed += self.GRAVITY * diff_time

        # Y out of bounds
        if self.y + self.h > cfg.GAME_HEIGHT:
            self.y = cfg.GAME_HEIGHT - self.h
            self.ySpeed = 0
            self.IN_GROUND = True

        # Checks collision in Y axis
        for wall in wallList:
            if self.__hasCollided(wall):
                # Collided from up
                if self.y < wall.y:
                    self.y = wall.y - self.h - 0.1
                    self.ySpeed = 0
                    self.IN_GROUND = True
                # Collided from down
                else:
                    self.y = wall.y + wall.h + 0.1
                    self.ySpeed = 0
        for spike in spikeList:
            if self.__hasCollided(spike):
                # Collided from up
                if self.y < spike.y:
                    self.DEAD = True
                # Collided from down
                else:
                    self.y = spike.y + spike.h + 0.1
                    self.ySpeed = 0

    def isDead(self):
        return self.DEAD

    # Go back to start of level
    def reset(self):
        self.x = self.xSpawn
        self.y = self.ySpawn
        self.xSpeed = 0
        self.ySpeed = 0
        self.DEAD = False
        self.IN_GROUND = False

        # Resets keyboard
        self.keysPressed = [False, False, False, False]

    def render(self, bufferSurface):
        self.sprite.render(bufferSurface, self.x, self.y)
