import pygame
import config as cfg
from image import Image
from checkbutton import CheckButton

class SettingsButtonList:
    def __init__ (self):
        self.BUTTON0 = 0
        self.BUTTON1 = 1
        self.BUTTON2 = 2

        selectedImage = Image("media/selectedcheckbutton.png", alpha=True)
        checkedImage = Image("media/checkedbutton.png", alpha=True)
        boxImage = Image("media/checkbuttonbox.png", alpha=True)

        button1 = CheckButton("media/button1.png", selectedImage, checkedImage, boxImage, 32, 32)
        button2 = CheckButton("media/button2.png", selectedImage, checkedImage, boxImage, 32, 96)
        button3 = CheckButton("media/button3.png", selectedImage, checkedImage, boxImage, 32, 160)

        self.button = [button1, button2, button3]
        self.button[self.BUTTON0].select()

    def selected(self):
        if self.button[self.BUTTON0].isSelected():
            return self.BUTTON0
        elif self.button[self.BUTTON1].isSelected():
            return self.BUTTON1
        else:
            return self.BUTTON2

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
        self.button[selected].toggleCheck()

    def render(self, bufferSurface):
        [button.render(bufferSurface) for button in self.button]
