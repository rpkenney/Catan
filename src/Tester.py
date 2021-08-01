import Player
import Tile
import GameGUI
import Dice
import Corner
import Road

corns = Corner.generate_regular_hexmap(3)
roads = Road.generate_road_df(corns)

roads['occupant'][0] = 'Robert'
roads['occupant'][1] = 'Robert'
roads['occupant'][10] = 'Robert'
roads['occupant'][11] = 'Robert'

test_len = Road.get_road_length(2, roads)
