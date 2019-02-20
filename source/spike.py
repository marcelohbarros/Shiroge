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
        self.x = x + 0.5
        self.y = y + 0.5
        self.h = self.sprite.h / cfg.GAME_SCALE - 1
        self.w = self.sprite.w / cfg.GAME_SCALE - 1
        # Mod 4 because it does not allow forbidden states to exist
        self.orientation = orientation % 4

    def render(self, bufferSurface):
        self.sprite.render(bufferSurface, self.x - 0.5, self.y - 0.5)

    def getOrientation(self):
        return self.orientation
