from menu import Menu
from level import Level
from settings import Settings
import pygame
import config as cfg

class Game:

    def __init__(self):

        # State constants
        self.MENU = 0
        self.LEVEL = 1
        self.SETTINGS = 2
        self.QUIT = 3
        
        # Initializing pygame
        pygame.init()
        self.window = pygame.display.set_mode((int(cfg.SCREEN_WIDTH / cfg.WINDOW_SCALE), int(cfg.SCREEN_HEIGHT / cfg.WINDOW_SCALE)))
        self.surface = pygame.Surface((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
        pygame.display.set_caption('Shiroge')
        pygame.key.set_repeat(200, 80)

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
