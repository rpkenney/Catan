import Player
import Tile
import GameGUI
import Dice
import Corner

def build_board(names,dim):
    
    corns = Corner.generate_regular_hexmap(dim)
    
    resources = ['b','r','l','s','w']
    resource_amounts = [3,3,4,4,4]

    players = Player.generate_players(names, resources)

    tiles = Tile.generate_tiles(resources, resource_amounts, corns, dim)
    
    return (corns, tiles, players)
    


#Script ---------------------------------------------------------

n = int(input("What type of board do you want to play on?: "))
numPlayers = int(input("How many people are playing?: "))
players = []

for i in range(numPlayers):
    players.append(input("Who is player " + str(i+1) + "?: "))

print(players)
ctp = build_board(players, n)

gui = GameGUI.GameGUI(ctp[1])

print("Number of Tiles: " + str(len(ctp[1])))
print("Number of Corners: " + str(len(ctp[0])))
print("Number of Players: " + str(len(ctp[2])))