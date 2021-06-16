import Player
import Tile
import GameGUI
import Dice
import Corner
import Presets

true = Presets.generate_regular_hexmap(3)

print(Corner.get_neighbor(27, true, 3))
print(Corner.get_neighbor(7, true, 3))
print(Corner.get_neighbor(63, true, 3))
print(Corner.get_neighbor(32, true, 3))
print(Corner.get_neighbor(33, true, 3))


"""
resources = ['b','r','l','s','w']
resource_amounts = [3,3,4,4,4]

names = ['Noah', 'Robert']
players = Player.generate_players(names, resources)

tiles = Tile.generate_tiles(resources, resource_amounts)

gui = GameGUI.GameGUI(tiles)
"""