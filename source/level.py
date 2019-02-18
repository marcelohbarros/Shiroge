import pygame
from player import Player
from image import Image
from wall import Wall
from spike import Spike
from grass import Grass
import config as cfg

class Level:

    def __init__(self):
        self.player = Player()
        self.lifeImage = Image("media/heart.png", alpha=True)
        self.lifes = 3

        # Tile constants
        NONE = 0
        DIRT = 1
        BRICK = 2
        SPIKE = 3
        PLAYER = 4
        GRASS = 5

        # Images for objects on level
        brickImage = Image("media/brick.png")
        dirtImage = Image("media/dirt.png")
        grassImage = Image("media/grass.png", alpha=True)
        spikeImage = Image("media/spike.png", alpha=True)

        # Tile size used on loading level elements scaled to game proportions
        TILE_SIZE = brickImage.w / cfg.GAME_SCALE

        # Containers with object list elements in level
        self.wallList = []
        self.spikeList = []
        self.grassList = []

        levelFile = open("level/1", "r")

        # Offset used on placing objects
        Y_OFFSET = cfg.GAME_HEIGHT % TILE_SIZE - TILE_SIZE

        # Loading level file
        for yPos, row in enumerate(levelFile):
            for xPos, element in enumerate(row.split(",")):
                tile = int(element)
                if tile == DIRT:
                    self.wallList.append(Wall(dirtImage, xPos * TILE_SIZE, Y_OFFSET + yPos * TILE_SIZE))
                elif tile == BRICK:
                    self.wallList.append(Wall(brickImage, xPos * TILE_SIZE, Y_OFFSET + yPos * TILE_SIZE))
                elif tile == SPIKE:
                    self.spikeList.append(Spike(spikeImage, xPos * TILE_SIZE, Y_OFFSET + yPos * TILE_SIZE))
                elif tile == PLAYER:
                    self.player = Player(xPos * TILE_SIZE, Y_OFFSET + yPos * TILE_SIZE)
                elif tile == GRASS:
                    self.grassList.append(Grass(grassImage, xPos * TILE_SIZE, Y_OFFSET + yPos * TILE_SIZE))

        levelFile.close()

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

        # Render player
        self.player.render(game.surface)

        # Render containers
        [wall.render(game.surface) for wall in self.wallList]
        [spike.render(game.surface) for spike in self.spikeList]
        [grass.render(game.surface) for grass in self.grassList]

        # Render hearts indicating number of lifes
        for i in range(0, self.lifes):
            self.lifeImage.render(game.surface, 8+24*i, 8)

        # Scale surface buffer to screen surface
        pygame.transform.scale(game.surface, (game.window.get_width(), game.window.get_height()), game.window)

        # Update image
        pygame.display.flip()
