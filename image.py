import pygame

# Wrapper for pygame.image class
class Image:

    def __init__(self):
        self.surface = None
        self.w, self.h = 0, 0

    def __init__(self, path):
        self.surface = pygame.image.load(path).convert()
        rect = self.surface.get_rect()
        self.w, self.h = rect.w, rect.h

    def render(self, game, x = 0, y = 0):
        rect = pygame.Rect(x * game.SCALE, y * game.SCALE, self.w * game.SCALE, self.h * game.SCALE)
        render_surface = pygame.transform.scale(self.surface, (rect.w, rect.h))
        game.window.blit(render_surface, rect)
