import Player
import Tile
import GameGUI
import Dice
import Corner


dim = 3
width = dim*4-1

true = Corner.generate_regular_hexmap(dim)

"""
print(Corner.get_neighbor(27, true, dim))
print(Corner.get_neighbor(7, true, dim))
print(Corner.get_neighbor(63, true, dim))
print(Corner.get_neighbor(32, true, dim))
print(Corner.get_neighbor(33, true, dim))
"""

print(true)

resources = ['b','r','l','s','w']
resource_amounts = [3,3,4,4,4]

names = ['Noah', 'Robert']
players = Player.generate_players(names, resources)

tiles = Tile.generate_tiles(resources, resource_amounts, true, width)

print(len(tiles))
print(tiles)

#gui = GameGUI.GameGUI(tiles)
