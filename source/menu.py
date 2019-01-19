import pygame
from image import Image
from buttonlist import ButtonList

class Menu:

    # Menu contains background image and buttons
    def __init__(self):
        self.background = Image("media/menubg.png")
        self.buttonList = ButtonList()

    def handleInputs(self, game):
        # Polling events
        for event in pygame.event.get():
            # Quit on closing window or pressing esc
            if event.type == pygame.QUIT:
                game.setState(game.QUIT)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.setState(game.QUIT)
                
                # Change selected button on arrows selected
                elif event.key == pygame.K_DOWN:
                    self.buttonList.selectNext()
                elif event.key == pygame.K_UP:
                    self.buttonList.selectPrevious()
                
                # Goes to next state on enter pressed
                elif event.key == pygame.K_RETURN:
                    if self.buttonList.selected() == self.buttonList.PLAY:
                        game.setState(game.LEVEL)
                    elif self.buttonList.selected() == self.buttonList.SETTINGS:
                        game.setState(game.SETTINGS)
                    elif self.buttonList.selected() == self.buttonList.QUIT:
                        game.setState(game.QUIT)

    def logic(self, game):
        game.changeState()

    def render(self, game):
        # Clear buffer and window surfaces
        game.window.fill((0, 0, 0))
        game.surface.fill((0, 0, 0))
        
        # Render menu elements
        self.background.render(game.surface)
        self.buttonList.render(game.surface)

        # Scale surface buffer to screen surface
        pygame.transform.scale(game.surface, (game.window.get_width(), game.window.get_height()), game.window)

        # Update image
        pygame.display.flip()
