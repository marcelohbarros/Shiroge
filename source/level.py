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
        self.NONE = 0
        self.DIRT = 1
        self.BRICK = 2
        self.SPIKE = 3
        self.PLAYER = 4
        self.GRASS = 5

        # Images for objects on level
        self.brickImage = Image("media/brick.png")
        self.dirtImage = Image("media/dirt.png")
        self.grassImage = Image("media/grass.png", alpha=True)
        self.spikeImage = Image("media/spike.png", alpha=True)

        # Tile size used on loading level elements scaled to game proportions
        self.TILE_SIZE = self.brickImage.w / cfg.GAME_SCALE

        # Containers with object list elements in level
        self.wallList = []
        self.spikeList = []
        self.grassList = []

        # Offset used on placing objects
        self.Y_OFFSET = cfg.GAME_HEIGHT % self.TILE_SIZE - self.TILE_SIZE

        # First level
        self.level = 1
        self.loadLevel(self.level)

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
        if self.player.hasWon():
            self.loadLevel(1)
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

    # Loading level file
    def loadLevel(self, level):
        path = "level/" + str(level)
        levelFile = open(path, "r")

        # Loads elements in level
        for yPos, row in enumerate(levelFile):
            for xPos, element in enumerate(row.split(",")):
                tile = int(element)
                if tile == self.DIRT:
                    self.wallList.append(Wall(self.dirtImage, xPos * self.TILE_SIZE, self.Y_OFFSET + yPos * self.TILE_SIZE))
                elif tile == self.BRICK:
                    self.wallList.append(Wall(self.brickImage, xPos * self.TILE_SIZE, self.Y_OFFSET + yPos * self.TILE_SIZE))
                elif tile == self.SPIKE:
                    self.spikeList.append(Spike(self.spikeImage, xPos * self.TILE_SIZE, self.Y_OFFSET + yPos * self.TILE_SIZE))
                elif tile == self.PLAYER:
                    self.player = Player(xPos * self.TILE_SIZE, self.Y_OFFSET + yPos * self.TILE_SIZE)
                elif tile == self.GRASS:
                    self.grassList.append(Grass(self.grassImage, xPos * self.TILE_SIZE, self.Y_OFFSET + yPos * self.TILE_SIZE))

        levelFile.close()
