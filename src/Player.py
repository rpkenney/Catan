def generate_players(names):
    '''
    Generates a dataframe full of players with information such as their name, the number of buildings remaining,
    and the cards that they have
    
    Parameters
    -----------
    an array of names to be created as players
    
    Returns
    -----------
    a array containing information about each player
    '''
    players = []
    for name in names:
        player = {'name':name,'vp':0,'sm':5,'rd':15,'ct':4,
                  'res':{'l':0,'b':0,'r':0,'w':0,'s':0},'dc':[]}
        players.append(player)       
    return players