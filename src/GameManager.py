import Player
import Tile

resources = ['b','r','l','s','w']
resource_amounts = [3,3,4,4,4]

players = Player.generate_players(['Noah', 'Robert'], resources)

Tile.generate_tiles(resources, resource_amounts)


