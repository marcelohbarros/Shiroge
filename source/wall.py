from image import Image
import config as cfg

class Wall:
    def __init__(self, image, x=0, y=0):
        # Set height and width from image size
        self.sprite = image
        self.x = x + 0.5
        self.y = y + 0.5
        self.h = self.sprite.h / cfg.GAME_SCALE - 1
        self.w = self.sprite.w / cfg.GAME_SCALE - 1

    def render(self, bufferSurface):
        self.sprite.render(bufferSurface, self.x - 0.5, self.y - 0.5)
