import Player
import Corner
import Road
import networkx as nx
import matplotlib.pyplot as plt

players = Player.generate_players(['Noah', 'Robert'])

corners = Corner.generate_corners()

roads = Road.load_roads()

game_map = nx.Graph()
game_map.add_nodes_from(corners)
for i in range(roads.shape[0]):
    game_map.add_edge(roads['node1'][i], roads['node2'][i])
    

plt.figure()
pos = nx.spring_layout(game_map)
nx.draw(game_map,pos,with_labels = True)