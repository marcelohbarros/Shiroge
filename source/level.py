import pygame
from player import Player
from image import Image
from wall import Wall
from spike import Spike

class Level:

    def __init__(self):
        self.player = Player()
        self.lifeImage = Image("media/heart.png", alpha=True)
        self.lifes = 3

        brickImage = Image("media/brick.png")
        dirtImage = Image("media/dirt.png")
        # Object containing all wall elements in level
        self.wallList = []
        self.wallList.append(Wall(dirtImage, 32, 264))

        spikeImage = Image("media/spike.png", alpha=True)
        # Object containing all spike elements in level
        self.spikeList = []
        self.spikeList.append(Spike(spikeImage, 96, 328))

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
        self.player.move(self.wallList, self.spikeList)
        if self.player.isDead():
            self.lifes -= 1
            if self.lifes >= 0:
                self.player.reset()
            else:
                game.setState(game.MENU)

    def render(self, game):
        # Clear buffer and window surfaces
        game.window.fill((0, 0, 0))
        game.surface.fill((0, 0, 0))

        [wall.render(game.surface) for wall in self.wallList]
        [spike.render(game.surface) for spike in self.spikeList]
        self.player.render(game.surface)
        # Render hearts indicating number of lifes
        for i in range(0, self.lifes):
            self.lifeImage.render(game.surface, 8+24*i, 8)

        # Scale surface buffer to screen surface
        pygame.transform.scale(game.surface, (game.window.get_width(), game.window.get_height()), game.window)

        # Update image
        pygame.display.flip()
