import pygame
from player import Player
from image import Image
from wall import Wall

class Level:

    def __init__(self):
        self.player = Player() 
        brickImage = Image("media/brick.png")
        dirtImage = Image("media/dirt.png")
        self.wallList = []
        self.wallList.append(Wall(dirtImage, 0, 328))

    def handleInputs(self, game):
        # Polling events
        for event in pygame.event.get():
            self.player.handleInputs(event)
            # Quit on closing window or pressing esc
            if event.type == pygame.QUIT:
                game.setState(game.QUIT)
            elif event.type == pygame.KEYDOWN:
                # Go to menu
                if event.key == pygame.K_ESCAPE:
                    game.setState(game.MENU)

    def logic(self, game):
        game.changeState()
        self.player.move(self.wallList)

    def render(self, game):
        # Clear buffer and window surfaces
        game.window.fill((0, 0, 0))
        game.surface.fill((0, 0, 0))

        [wall.render(game.surface) for wall in self.wallList]
        self.player.render(game.surface)

        # Scale surface buffer to screen surface
        pygame.transform.scale(game.surface, (game.window.get_width(), game.window.get_height()), game.window)

        # Update image
        pygame.display.flip()
