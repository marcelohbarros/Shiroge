import pygame
import config as cfg
from image import Image
from checkbutton import CheckButton
from button import Button

class SettingsButtonList:
    def __init__ (self):
        self.FULLSCREEN = 0
        self.HARDCOREMODE = 1
        self.RETURN = 2

        # Load assets for check buttons
        selectedImage = Image("media/selectedcheckbutton.png", alpha=True)
        checkedImage = Image("media/checkedbutton.png", alpha=True)
        boxImage = Image("media/checkbuttonbox.png", alpha=True)

        fullscreenButton = CheckButton("media/fullscreenButton.png", selectedImage, checkedImage, boxImage, 32, 32, cfg.fullscreen)
        hardcoreModeButton = CheckButton("media/hardcoremodebutton.png", selectedImage, checkedImage, boxImage, 32, 96, cfg.hardcoreMode)

        # Load assets for button
        selectedImage = Image("media/selectedbutton.png", alpha=True)
        returnButton = Button("media/returnbutton.png", selectedImage, 272, 296)

        self.button = [fullscreenButton, hardcoreModeButton, returnButton]
        self.button[self.FULLSCREEN].select()

    def handleMouseInput(self, game):
        # Checks if left mouse button was clicked
        if pygame.mouse.get_pressed()[0]:
            mousePos = [x * cfg.WINDOW_SCALE / cfg.GAME_SCALE for x in pygame.mouse.get_pos()]

            # Get button hitbox and check collision
            fullscreenButtonRect = self.button[self.FULLSCREEN].getRect()
            if fullscreenButtonRect.collidepoint(mousePos):
                self.button[self.FULLSCREEN].toggleCheck()
                selected = self.selected()
                self.button[selected].unselect()
                self.button[self.FULLSCREEN].select()
                return self.FULLSCREEN

            hardcoreModeButtonRect = self.button[self.HARDCOREMODE].getRect()
            if hardcoreModeButtonRect.collidepoint(mousePos):
                self.button[self.HARDCOREMODE].toggleCheck()
                selected = self.selected()
                self.button[selected].unselect()
                self.button[self.HARDCOREMODE].select()
                return self.HARDCOREMODE

            returnButtonRect = self.button[self.RETURN].getRect()
            if returnButtonRect.collidepoint(mousePos):
                game.setState(game.MENU)
                return None

    def selected(self):
        if self.button[self.FULLSCREEN].isSelected():
            return self.FULLSCREEN
        elif self.button[self.HARDCOREMODE].isSelected():
            return self.HARDCOREMODE
        else:
            return self.RETURN

    def selectNext(self):
        selected = self.selected()
        self.button[selected].unselect()
        self.button[(selected + 1) % len(self.button)].select()

    def selectPrevious(self):
        selected = self.selected()
        self.button[selected].unselect()
        self.button[(selected - 1) % len(self.button)].select()

    def toggleCheck(self):
        selected = self.selected()
        if selected != self.RETURN:
            self.button[selected].toggleCheck()

    def render(self, bufferSurface):
        [button.render(bufferSurface) for button in self.button]
