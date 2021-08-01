import networkx as nx

import pandas as pd
import Corner

def generate_road_df(corners):
    roads = []
    for corner in corners:
        neighbors = Corner.get_neighbors(corner,corners,3)
        for neighbor in neighbors:
            road = {corner, neighbor}
            if road not in roads:
                roads.append(road)
                
    labels = ['c1', 'c2','occupant']
    roads_df = pd.DataFrame(columns=labels)
    for road in roads:
        road = list(road)
        row = pd.DataFrame([[road[0], road[1], None]], columns = labels)
        roads_df = roads_df.append(row, ignore_index = True)

    return roads_df

def get_longest_road(roads):
    longest = 0
    
    for road in roads.index:
        c = roads['c1'][road]
        if roads['occupant'][road] != None:
            get_road_length(c, roads)

def get_road_length(corner, roads):
    branch_lengths = []
    
    c1 = roads[roads['c1'] == corner]
    c2 = roads[roads['c2'] == corner] 
    
    branches = pd.concat([c1, c2])
    branches = branches.index[branches['occupant'].notnull()]
    
    for branch in branches:
        branch_lengths.append(get_branch_length(corner, roads, None, branch))
    
    return sum(branch_lengths)

def get_branch_length(corner, roads, uc, branch):
    longest = 0
     
    if branch == None:
        c1 = roads[roads['c1'] == corner]
        c2 = roads[roads['c2'] == corner] 
        connections = pd.concat([c1, c2])
        connections = connections.index[connections['occupant'].notnull()]
    else:
        connections = [branch]
    
    if uc == None:
        uc = []
    
    copy = uc.copy()
    
    for connection in connections:
        nc = roads['c1'][connection]
        if roads['c2'][connection] != corner:
            nc = roads['c2'][connection]
        if nc in uc:
            continue
        uc.append(corner)
        curr_len = get_branch_length(nc, roads, uc, None) + 1
        if curr_len > longest:
            longest = curr_len
        uc = copy
    return longest
        


if __name__ == "__main__":
    roads = generate_road_df(Corner.generate_regular_hexmap(3))
    get_longest_road(roads)
