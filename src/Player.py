import pandas as pd

def generate_players(names):
    '''
    Generates a dataframe full of players with information such as their name, the number of buildings remaining,
    and the cards that they have
    
    Paramaters
    -----------
    an array of names to be created as players
    
    Returns
    -----------
    a dataframe containing information about each player
    '''
    labels = ['name','victory points','#settlement','#roads','#cities','resources','dev cards']
    players = pd.DataFrame(columns=labels)
    for name in names:
        player = {'name':name,'victory points':0,'#settlement':5,'#roads':15,'#cities':4,'resources':[],'dev cards':[]}
        players = players.append(player, ignore_index=True)       
    return players