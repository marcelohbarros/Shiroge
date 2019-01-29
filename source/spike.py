from image import Image
import config as cfg

class Spike:
    def __init__(self, image, x=0, y=0):
        # Set height and width from image size
        self.sprite = image
        self.x = x
        self.y = y
        self.h = self.sprite.h / cfg.GAME_SCALE
        self.w = self.sprite.w / cfg.GAME_SCALE

    def render(self, bufferSurface):
        self.sprite.render(bufferSurface, self.x, self.y)
