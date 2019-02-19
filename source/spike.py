from image import Image
import config as cfg

class Spike:

    def __init__(self, image, x=0, y=0, orientation=0):
        self.UP = 0
        self.DOWN = 2
        self.LEFT = 1
        self.RIGHT = 3

        # Set height and width from image size
        self.sprite = image
        self.x = x
        self.y = y
        self.h = self.sprite.h / cfg.GAME_SCALE
        self.w = self.sprite.w / cfg.GAME_SCALE
        # Mod 4 because it does not allow forbidden states to exist
        self.orientation = orientation % 4

    def render(self, bufferSurface):
        self.sprite.render(bufferSurface, self.x, self.y)

    def getOrientation(self):
        return self.orientation
