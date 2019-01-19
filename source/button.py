import pygame
from image import Image

class Button:
    # Loads text image, but selection image is loaded externally
    def __init__(self, path, selectedImage, x, y):
            self.textImage = Image(path)
            self.selectedImage = selectedImage
            self.x = x
            self.y = y
            self.selected = False

    def isSelected(self):
        return self.selected

    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def render(self, bufferSurface):
        self.textImage.render(bufferSurface, self.x, self.y)
        if self.selected:
            self.selectedImage.render(bufferSurface, self.x, self.y)
        
