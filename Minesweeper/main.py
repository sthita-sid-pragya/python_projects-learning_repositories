from game import Game
from board import Board
size = (20, 50)
prob = 0.2
board = Board(size, prob)
screenSize = (1700, 800)
game = Game(board, screenSize)
game.run()