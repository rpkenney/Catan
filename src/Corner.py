def generate_corners():
    return list(range(1, 54))

"""
parameters
    corner - int value of the corner of interest
    trueCorners - corners that are used from the square map
"""
def get_neighbor(corner, trueCorners, dim):
    width = 11
    neighbors = []
    
    if corner % width != 10:
        neighbors.append(corner+1)
    if corner % width != 0:
        neighbors.append(corner-1)
    
    if (corner + dim) % 2 == 0:
        neighbors.append(corner-width)
    else:
        neighbors.append(corner+width)
    
    neighbors = [x for x in neighbors if x in trueCorners]
    
    return neighbors
        
    
    
    