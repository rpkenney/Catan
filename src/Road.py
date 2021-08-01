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

def get_longest_road(corners, roads):
    longest = 0
    
    for corner in range(len(corners)):
        curr = get_road_length(corner, roads)
        if curr > longest:
            longest = curr
            
    return longest
        

def get_road_length(corner, roads):
    branch_lengths = []
    
    branches = get_adj_roads(corner, roads).index
    
    for branch in branches:
        branch_lengths.append(get_branch_length(corner, roads, start = branch))
    
    return sum(branch_lengths)

def get_branch_length(corner, roads, used_corners = [], start = None):
    longest = 0
    
    if start == None:
        connections = get_adj_roads(corner, roads).index
    else:
        connections = [start]

    copy = used_corners.copy()
    
    #base case is when length of connections is 0 so 0 is returned
    for connection in connections:
        new_corner = roads['c1'][connection]
        if roads['c2'][connection] != corner:
            new_corner = roads['c2'][connection]
        if new_corner in used_corners:
            continue
        used_corners.append(corner)
        #recursive step
        curr_len = get_branch_length(new_corner, roads, used_corners) + 1
        if curr_len > longest:
            longest = curr_len
        used_corners = copy

    return longest
        

def get_adj_roads(corner, roads, include_vacant = False, ignore_index = False):
    c1 = roads[roads['c1'] == corner]
    c2 = roads[roads['c2'] == corner] 
    connections = pd.concat([c1, c2], ignore_index = ignore_index)
    if not include_vacant:
        connections = connections[connections['occupant'].notnull()]
    
    return connections
    

if __name__ == "__main__":
    roads = generate_road_df(Corner.generate_regular_hexmap(3))
    get_longest_road(roads)
