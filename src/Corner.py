"""
Generate a map that is in the shape of a regular hexagon with n tiles on each side

parameter:
    dim - the n number of tiles on each side
    
return:
    corners - whitelist of corners that exist on the map
"""

def generate_regular_hexmap(dim = 3):
    
    rows = dim * 2
    cols = dim * 4 - 1
    
    corners = range(0, rows*cols-1)
    notCorners = []

    for i in range(1, dim):
        for j in range(dim-i,0,-1):
            notCorners.append(cols*(j-1) + i-1) #Top left
            notCorners.append(cols*j-i) #Top right
            notCorners.append(cols*(rows-i)+j-1) #Bottom left
            notCorners.append(cols*(rows-j+1)-i) #Bottom right
    
    corners = [x for x in corners if x not in notCorners]
    
    return tuple(corners)

"""
parameters
    corner - int value of the corner of interest
    trueCorners - corners that are used from the square map
    dim - number of tiles on the side of a regular hexmap
    
return
    neighbors - tuple of neighboring corners
"""
def get_neighbors(corner, trueCorners = [2,3,4,5,6,7,8,12,13,14,15,16,17,18,19,20,22,23,24,
                                   25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,
                                   42,43,45,46,47,48,49,50,51,52,53,57,58,59,60,61,62,63], dim = 3):
    width = 4 * dim - 1
    neighbors = []
    
    if corner % width != width-1:
        neighbors.append(corner+1)
    if corner % width != 0:
        neighbors.append(corner-1)
    
    if (corner + dim) % 2 == 0:
        neighbors.append(corner-width)
    else:
        neighbors.append(corner+width)
    
    neighbors = [x for x in neighbors if x in trueCorners]
    
    return neighbors
        
def get_adjacent_tiles(corner, board, dim = 3):
    width = 4 * dim - 1
    tiles = []
    
    if corner%2 == 0:
        tiles = [corner//2,corner//2-1,(corner-width)//2]
    else:
        tiles = [corner//2,(corner-width)//2,(corner-width)//2-1]
    
    return [x for x in tiles if x in board]

    
    