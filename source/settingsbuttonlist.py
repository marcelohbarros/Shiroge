import pygame
import config as cfg
from image import Image
from checkbutton import CheckButton
from button import Button

class SettingsButtonList:
    def __init__ (self):
        self.FULLSCREEN = 0
        self.BUTTON1 = 1
        self.BUTTON2 = 2
        self.RETURN = 3

        # Load assets for check buttons
        selectedImage = Image("media/selectedcheckbutton.png", alpha=True)
        checkedImage = Image("media/checkedbutton.png", alpha=True)
        boxImage = Image("media/checkbuttonbox.png", alpha=True)

        fullscreenButton = CheckButton("media/fullscreenButton.png", selectedImage, checkedImage, boxImage, 32, 32, cfg.fullscreen)
        button2 = CheckButton("media/button2.png", selectedImage, checkedImage, boxImage, 32, 96)
        button3 = CheckButton("media/button3.png", selectedImage, checkedImage, boxImage, 32, 160)

        # Load assets for button
        selectedImage = Image("media/selectedbutton.png", alpha=True)
        returnButton = Button("media/returnbutton.png", selectedImage, 272, 296)

        self.button = [fullscreenButton, button2, button3, returnButton]
        self.button[self.FULLSCREEN].select()

    def selected(self):
        if self.button[self.FULLSCREEN].isSelected():
            return self.FULLSCREEN
        elif self.button[self.BUTTON1].isSelected():
            return self.BUTTON1
        elif self.button[self.BUTTON2].isSelected():
            return self.BUTTON2
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

    def check(self):
        selected = self.selected()
        if selected != self.RETURN:
            self.button[selected].toggleCheck()

    def render(self, bufferSurface):
        [button.render(bufferSurface) for button in self.button]
