import pandas as pd
import networkx as nx

def load_roads():
    road_df = pd.read_csv('data/map.csv',header=0)
    return road_df