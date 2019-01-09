from menu import Menu
from level import Level
from settings import Settings
import pygame

class Game:

    def __init__(self):

        # State constants
        self.MENU = 0
        self.LEVEL = 1
        self.SETTINGS = 2
        self.QUIT = 3

        # Initializing pygame
        
        # Screen constants
        self.WIDTH = 640
        self.HEIGHT = 360
        self.SCALE = 2

        # Initializing pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH * self.SCALE, self.HEIGHT * self.SCALE))
        pygame.display.set_caption('Pygame game')

        # Game starts on menu
        self.state = Menu()

        self.finished = False
        self.nextState = None

    def handleInputs(self):
        self.state.handleInputs(self)

    def logic(self):
        self.state.logic(self)

    def render(self):
        self.state.render(self)

    def hasFinished(self):
        return self.finished

    def setState(self, state):
        if state == self.MENU:
            self.nextState = self.MENU
        elif state == self.LEVEL:
            self.nextState = self.LEVEL
        elif state == self.SETTINGS:
            self.nextState = self.SETTINGS
        elif state == self.QUIT:
            self.nextState = self.QUIT

    def changeState(self):
        if self.nextState == self.MENU:
            self.state = Menu()
            self.nextState = None
        elif self.nextState == self.LEVEL:
            self.state = Level()
            self.nextState = None
        elif self.nextState == self.SETTINGS:
            self.state = Settings()
            self.nextState = None
        elif self.nextState == self.QUIT:
            self.finished = True
            self.nextState = None
