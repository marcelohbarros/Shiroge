import pygame
import config as cfg

# Wrapper for pygame.image class
class Image:

    def __init__(self):
        self.surface = None
        self.w, self.h = 0, 0

    def __init__(self, path, alpha = False):
        # Load surface on original resolution
        original_surface = pygame.image.load(path)
        w = original_surface.get_width()
        h = original_surface.get_height()

        # Transform surface into max resolution
        if alpha:
            self.surface = pygame.transform.scale(original_surface, (int(w * cfg.GAME_SCALE), int(h * cfg.GAME_SCALE))).convert_alpha()
        else:
            self.surface = pygame.transform.scale(original_surface, (int(w * cfg.GAME_SCALE), int(h * cfg.GAME_SCALE))).convert()
        self.w = self.surface.get_width()
        self.h = self.surface.get_height()

    def render(self, bufferSurface, x = 0, y = 0):
        rect = pygame.Rect(x * cfg.GAME_SCALE, y * cfg.GAME_SCALE, self.w, self.h)
        bufferSurface.blit(self.surface, rect)
