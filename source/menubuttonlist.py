import pygame
import config as cfg
from image import Image
from button import Button
from game import * 

class MenuButtonList:
    def __init__ (self):
        self.PLAY = 0
        self.SETTINGS = 1
        self.QUIT = 2

        selectedImage = Image("media/selectedbutton.png", alpha=True)

        playButton = Button("media/playbutton.png", selectedImage, 272, 96)
        settingsButton = Button("media/settingsbutton.png", selectedImage, 272, 160)
        quitButton = Button("media/quitbutton.png", selectedImage, 272, 224)

        self.button = [playButton, settingsButton, quitButton]
        self.button[self.PLAY].select()

    def handleMouseInput(self, game):
        # Checks if left mouse button was clicked
        if pygame.mouse.get_pressed()[0]:
            mousePos = [x * cfg.WINDOW_SCALE / cfg.GAME_SCALE for x in pygame.mouse.get_pos()]

            # Get button hitbox and check collision
            playButtonRect = self.button[self.PLAY].getRect()
            if playButtonRect.collidepoint(mousePos):
                game.setState(game.LEVEL)
            settingsButtonRect = self.button[self.SETTINGS].getRect()
            if settingsButtonRect.collidepoint(mousePos):
                game.setState(game.SETTINGS)
            quitButtonRect = self.button[self.QUIT].getRect()
            if quitButtonRect.collidepoint(mousePos):
                game.setState(game.QUIT)

    def selected(self):
        if self.button[self.PLAY].isSelected():
            return self.PLAY
        elif self.button[self.SETTINGS].isSelected():
            return self.SETTINGS
        else:
            return self.QUIT

    def selectNext(self):
        selected = self.selected()
        self.button[selected].unselect()
        self.button[(selected + 1) % len(self.button)].select()

    def selectPrevious(self):
        selected = self.selected()
        self.button[selected].unselect()
        self.button[(selected - 1) % len(self.button)].select()

    def render(self, bufferSurface):
        [button.render(bufferSurface) for button in self.button]
