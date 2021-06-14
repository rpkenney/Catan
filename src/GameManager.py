import Player
import Tile
import GameGUI

resources = ['b','r','l','s','w']
resource_amounts = [3,3,4,4,4]

players = Player.generate_players(['Noah', 'Robert'], resources)

tiles = Tile.generate_tiles(resources, resource_amounts)

gui = GameGUI.GameGUI(tiles)