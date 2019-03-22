import pygame
from image import Image
from timer import Timer
import config as cfg

class Player:

    def __init__(self, x=0, y=0):
        self.sprite = Image("media/player.png", alpha=True)

        # Values from initial position are reused on player death
        self.xSpawn = x + 0.05
        self.ySpawn = y + 0.05

        self.x = self.xSpawn
        self.y = self.ySpawn
        self.h = self.sprite.h / cfg.GAME_SCALE - 0.1
        self.w = self.sprite.w / cfg.GAME_SCALE - 0.1
        self.xSpeed = 0
        self.ySpeed = 30

        self.timer = Timer()
        
        self.keysPressed = [False, False, False, False]
        self.UP = 0
        self.DOWN = 1
        self.LEFT = 2
        self.RIGHT = 3

        self.X_SPEED = 200
        self.JUMP_SPEED = 350
        self.GRAVITY = 600
        self.MAX_Y_SPEED = 600

        self.inGround = False
        self.usedDownJump = False
        self.dead = False
        self.won = False

    def handleInputs(self, event):
        # Pressing key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if not self.keysPressed[self.UP]:
                    self.keysPressed[self.UP] = True
                    self.MAX_Y_SPEED = 100
                    if self.inGround:
                        self.ySpeed = -self.JUMP_SPEED
                        self.inGround = False
            # Pressing down does the player fall quicker
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if not self.keysPressed[self.DOWN]:
                    self.keysPressed[self.DOWN] = True
                    if not self.usedDownJump and not self.inGround:
                        self.ySpeed += 300
                        self.usedDownJump = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if not self.keysPressed[self.LEFT]:
                    self.xSpeed -= self.X_SPEED
                    self.keysPressed[self.LEFT] = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if not self.keysPressed[self.RIGHT]:
                    self.xSpeed += self.X_SPEED
                    self.keysPressed[self.RIGHT] = True

        # Releasing key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.MAX_Y_SPEED = 600
                if self.keysPressed[self.UP]:
                    self.keysPressed[self.UP] = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if self.keysPressed[self.DOWN]:
                    self.keysPressed[self.DOWN] = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if self.keysPressed[self.LEFT] and not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_a]:
                    self.xSpeed += self.X_SPEED
                    self.keysPressed[self.LEFT] = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                if self.keysPressed[self.RIGHT] and not pygame.key.get_pressed()[pygame.K_RIGHT] and not pygame.key.get_pressed()[pygame.K_d]:
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

        # Move X
        self.x += self.xSpeed * diff_time
        
        # X out of bounds
        if self.x < 0 - self.w:
            self.x = 0 - self.w
            self.won = True
        elif self.x > cfg.GAME_WIDTH:
            self.x = cfg.GAME_WIDTH 
            self.won = True

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
                    if spike.getOrientation() == spike.LEFT:
                        self.dead = True
                    else:
                        self.x = spike.x - self.w - 0.1
                # Collided from right
                else:
                    if spike.getOrientation() == spike.RIGHT:
                        self.dead = True
                    else:
                        self.x = spike.x + spike.w + 0.1

        # Move Y
        self.y += self.ySpeed * diff_time
        self.ySpeed += self.GRAVITY * diff_time
        if self.ySpeed > self.MAX_Y_SPEED:
            self.ySpeed = self.MAX_Y_SPEED

        # inGround variable detected on player movement
        self.inGround = False

        # Y out of bounds
        if self.y + self.h > cfg.GAME_HEIGHT:
            self.y = cfg.GAME_HEIGHT - self.h
            self.ySpeed = 30
            self.inGround = True
            self.usedDownJump = False

        # Checks collision in Y axis
        for wall in wallList:
            if self.__hasCollided(wall):
                # Collided from up
                if self.y < wall.y:
                    self.y = wall.y - self.h - 0.01
                    self.ySpeed = 30
                    self.inGround = True
                    self.usedDownJump = False
                # Collided from down
                else:
                    self.y = wall.y + wall.h + 0.1
                    self.ySpeed = 0
        for spike in spikeList:
            if self.__hasCollided(spike):
                # Collided from up
                if self.y < spike.y:
                    if spike.getOrientation() == spike.UP:
                        self.dead = True
                    else:
                        self.y = spike.y - self.h - 0.01
                        self.ySpeed = 30
                        self.inGround = True
                        self.usedDownJump = False
                # Collided from down
                else:
                    if spike.getOrientation() == spike.DOWN:
                        self.dead = True
                    else:
                        self.y = spike.y + spike.h + 0.1
                        self.ySpeed = 0

    def isDead(self):
        return self.dead

    def hasWon(self):
        return self.won

    # Go back to start of level
    def reset(self):
        self.x = self.xSpawn
        self.y = self.ySpawn
        self.xSpeed = 0
        self.ySpeed = 30
        self.dead = False
        self.inGround = False

        # Resets keyboard
        self.keysPressed = [False, False, False, False]

    def render(self, bufferSurface):
        self.sprite.render(bufferSurface, self.x, self.y)
