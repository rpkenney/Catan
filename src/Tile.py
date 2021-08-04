import numpy as np

def generate_tiles(resources = ['b','r','l','s','w'], resource_amounts = [3,3,4,4,4],
                   true_corners = [2,3,4,5,6,7,8,12,13,14,15,16,17,18,19,20,22,23,24,
                                   25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,
                                   42,43,45,46,47,48,49,50,51,52,53,57,58,59,60,61,62,63], dim = 3):
    '''
    Generates a list of tuples, each representing the resource, and die value of a tile

    Parameters
    ----------
    resources : array
        a list of available resources
    resource_amounts : array
        a list of the amounts of each resource
    true_corners : array
        a list of corners that are on the map
    width
        an integer of the hexmap's width

    Returns
    -------
    board : array of tuples
        an array of randomized resource and die value tuples

    '''
    posID = []
    width = dim * 4 - 1
    
    for x in range(int(width*dim)):
        if x*2+dim%2 in true_corners and x*2+width+dim%2 in true_corners:
            posID.append(x)
    np.random.shuffle(posID)
    
    board = []
    die_vals = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    c = 0
    
    for i in range(len(resources)):
        for j in range(resource_amounts[i]):
            val = np.random.choice(die_vals)
            die_vals.remove(val)
            board.append((posID[c],resources[i], val))
            c += 1
    board.append((posID[c],'d',7))
    np.random.shuffle(board)            #Not sure  if this is necessary
    return sorted(tuple(board))


def get_adjacent_corners(tileID, corners = [2,3,4,5,6,7,8,12,13,14,15,16,17,18,19,20,22,23,24,
                                   25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,
                                   42,43,45,46,47,48,49,50,51,52,53,57,58,59,60,61,62,63], dim = 3):
    width = 4*dim - 1
    temp = [tileID*2-1,tileID*2,tileID*2+1,tileID*2+width-1,tileID*2+width,tileID*2+width+1]
    
    return [x for x in temp if x in corners]
    
    
    