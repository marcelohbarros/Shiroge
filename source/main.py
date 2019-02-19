from game import Game

game = Game()

while not game.hasFinished():
    game.handleInputs()
    game.logic()
    game.render()
game.quit()
