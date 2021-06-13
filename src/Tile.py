import numpy as np

def generate_tiles(resources, resource_amounts):
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
    