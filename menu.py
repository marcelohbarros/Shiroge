import pygame

class Menu:

    def __init__(self):
        return

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
        print("Now in menu")
        return
