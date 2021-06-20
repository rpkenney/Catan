import Player
import Tile
import GameGUI
import Dice
import Corner


dim = input("What type of board do you want to play on?: ")



def build_board(dim):
    
    corns = Corner.generate_regular_hexmap(dim)
    