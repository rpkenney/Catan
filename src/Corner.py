def generate_corners():
    return list(range(1, 54))

"""
parameters
    corner - int value of the corner of interest
    trueCorners - corners that are used from the square map
"""
def get_neighbor(corner, trueCorners):
    width = 11
    neighbors = []
    
    if corner % width != 0:
        neighbors.append(corner+1)
    if corner % width != 1:
        neighbors.append(corner-1)
    
    if corner % 2 == 0:
        neighbors.append(corner-width)
    else:
        neighbors.append(corner+width)
    
    for i in range(len(neighbors)):
        for j in range(len(trueCorners)):
            if neighbors[i] != trueCorners[j]:
                neighbors.remove(i)
        
    
    
    