import Player
import Tile
import GameGUI
import Dice
import Corner
import numpy as np

def build_board(names,dim):
    
    corns = Corner.generate_regular_hexmap(dim)
    
    resources = ['b','r','l','s','w']
    resource_amounts = [3,3,4,4,4]

    players = Player.generate_players(names, resources)

    tiles = Tile.generate_tiles(resources, resource_amounts, corns, dim)
    
    return (corns, tiles, players)
    
def start_game(game):
    players = game[2]
    np.random.shuffle(players)
    
    #Trying to iterate through each player in the dataframe and let them place
    #their first and second settlements. How do I add the settlement to smCorn list
    
    for p in players:
        
        print()
        print(p["name"] + "'s Turn")
        invalid = True
        corner = ""
        
        while invalid:
            corner = input("Where would you like to place your first settlement?: ")
            if int(corner) in game[0] :
                print("Valid corner choice")
                invalid = False
            else:
                print("Invalid Corner. Try again")
        
        p["smCorn"].append(corner)
        p["sm"] -= 1
    players.reverse()
    
    for p in players:
        
        print()
        print(p["name"] + "'s Turn")
        invalid = True
        corner = ""
        
        while invalid:
            corner = input("Where would you like to place your second settlement?: ")
            if int(corner) in game[0] :
                print("Valid corner choice")
                invalid = False
            else:
                print("Invalid Corner. Try again")
        
        p["smCorn"].append(corner)
        p["sm"] -= 1
    
    return (game[0],game[1],players)


#Script ---------------------------------------------------------

n = int(input("What type of board do you want to play on?: "))
numPlayers = int(input("How many people are playing?: "))
players = []

for i in range(numPlayers):
    players.append(input("Who is player " + str(i+1) + "?: "))

print(players)
ctp = build_board(players, n)

gui = GameGUI.GameGUI(ctp[1])

print("Number of Corners: " + str(len(ctp[0])))
print("Number of Tiles: " + str(len(ctp[1])))
print("Number of Players: " + str(len(ctp[2])))

ctp = start_game(ctp)

print(ctp[2])







