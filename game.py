from menu import Menu
from level import Level
from settings import Settings

class Game:

    def __init__(self):

        # State constants
        self.MENU = 0
        self.LEVEL = 1
        self.SETTINGS = 2
        self.QUIT = 3

        # Game starts on menu
        self.state = Menu()

        self.finished = False
        self.nextState = None

    def handleInputs(self):
        print("handling inputs")
        nextState = int(input())
        self.setState(nextState)
        self.state.handleInputs()

    def logic(self):
        print("logic")
        self.changeState()
        self.state.logic()

    def render(self):
        print("rendering")
        self.state.render()

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
