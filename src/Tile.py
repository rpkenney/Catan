import numpy as np

def generate_tiles(resources, resource_amounts,true_corners, width):
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
    
    for x in range (len(true_corners)//2):
        if x*2 in true_corners and x*2+width in true_corners:
            posID.append(x)
    
    
    board = []
    die_vals = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    
    for i in range(len(resources)):
        for j in range(resource_amounts[i]):
            val = np.random.choice(die_vals)
            die_vals.remove(val)
            board.append((resources[i], val))
    board.append(('d',7))
    np.random.shuffle(board)
    return board


def get_adjacent_corners(tileID, width):
    adj = [tileID*2-1,tileID*2,tileID*2+1,tileID*2+width-1,tileID*2+width,tileID*2+width+1]
    return adj
    
    
    