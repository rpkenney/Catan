import Player
import Tile
import GameGUI
import Dice

resources = ['b','r','l','s','w']
resource_amounts = [3,3,4,4,4]

names = ['Noah', 'Robert']
players = Player.generate_players(names, resources)

tiles = Tile.generate_tiles(resources, resource_amounts)

gui = GameGUI.GameGUI(tiles)