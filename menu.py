import pygame
from image import Image

class Menu:

    # Menu contains background image and buttons
    def __init__(self):
        self.background = Image("media/menubg.png")

    def handleInputs(self, game):
        # Polling events
        for event in pygame.event.get():
            # Quit on closing window or pressing esc
            if event.type == pygame.QUIT:
                game.setState(game.QUIT)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.setState(game.QUIT)
                # Go to level
                elif event.key == pygame.K_1:
                    game.setState(game.LEVEL)
                # Go to settings
                elif event.key == pygame.K_2:
                    game.setState(game.SETTINGS)

    def logic(self, game):
        game.changeState()

    def render(self, game):
        game.window.fill((0, 0, 0))
        self.background.render(game)
        pygame.display.flip()
