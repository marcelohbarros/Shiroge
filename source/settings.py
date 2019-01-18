import pygame

class Settings:

    def __init__(self):
        return

    def handleInputs(self, game):
        # Polling events
        for event in pygame.event.get():
            # Quit on closing window or pressing esc
            if event.type == pygame.QUIT:
                game.setState(game.QUIT)
            elif event.type == pygame.KEYDOWN:
                # Go to menu
                if event.key == pygame.K_ESCAPE:
                    game.setState(game.MENU)

    def logic(self, game):
        game.changeState()

    def render(self, game):
        print("Now in settings")
