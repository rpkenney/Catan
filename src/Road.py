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
        c1 = roads['c1'][road]
        print(c1)


if __name__ == "__main__":
    roads = generate_road_df(Corner.generate_regular_hexmap(3))
    get_longest_road(roads)
