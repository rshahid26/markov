import networkx as nx
import matplotlib.pyplot as plt
from markov import MarkovChain
import random

# Plot the Markov Chain using NetworkX and Matplotlib
def plot_graph(mc):
    G = nx.DiGraph()
    # Add nodes
    for v in mc.adj_list.keys():
        G.add_node(v)
    # Add edges
    for v, edges in mc.adj_list.items():
        for w, weight in edges:
            G.add_edge(v, w, weight=weight)

    # Create a dictionary that maps a color to each communication class
    scc = mc.kosaraju()
    vertex_colors = {}
    for _class in scc:
        color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
        for vertex in _class:
            vertex_colors[vertex] = color

    # Plot the graph with a common color to every communication class
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color=[vertex_colors.get(node, 'white') for node in G.nodes()], with_labels=True)
    plt.show()


# Example Discrete-Time Markov Chain
edges = [
    (1, 1, 0.1),
    (1, 2, 0.2),
    (1, 3, 0.3),
    (1, 4, 0.4),
    (2, 1, 0.2),
    (2, 2, 0.3),
    (2, 3, 0.4),
    (2, 4, 0.1),
    (3, 1, 0.3),
    (3, 2, 0.4),
    (3, 3, 0.1),
    (3, 4, 0.2),
    (4, 1, 0.4),
    (4, 2, 0.1),
    (4, 3, 0.2),
    (4, 4, 0.3),
    (5, 1, 0.1),
    (5, 2, 0.2),
    (5, 3, 0.3),
    (5, 4, 0.4),
    (6, 1, 0.2),
    (6, 2, 0.3),
    (6, 3, 0.4),
    (6, 4, 0.1),
    (7, 1, 0.3),
    (7, 2, 0.4),
    (7, 3, 0.1),
    (7, 4, 0.2),
    (8, 1, 0.4),
    (8, 2, 0.1),
    (8, 3, 0.2),
    (8, 4, 0.3),
    (9, 1, 0.1),
    (9, 2, 0.2),
    (9, 3, 0.3),
    (9, 4, 0.4),
    (10, 1, 0.2),
    (10, 2, 0.3),
    (10, 3, 0.4),
    (10, 4, 0.1),
    (11, 1, 0.3),
    (11, 2, 0.4),
    (11, 3, 0.1),
    (11, 4, 0.2),
    (12, 1, 0.4),
    (12, 2, 0.1),
    (12, 3, 0.2),
    (12, 4, 0.3),
    (13, 1, 0.1),
    (13, 2, 0.2),
    (13, 3, 0.3),
    (13, 4, 0.4),
    (14, 1, 0.2),
    (14, 2, 0.3),
    (14, 3, 0.4),
    (14, 4, 0.1),
    (15, 1, 0.3),
    (15, 2, 0.4),
    (15, 3, 0.1),
    (15, 4, 0.2),
    (16, 1, 0.4),
    (16, 2, 0.1),
    (16, 3, 0.2),
    (16, 4, 0.3),
    (17, 1, 0.1),
    (17, 2, 0.2),
    (17, 3, 0.3),
    (17, 4, 0.4),
    (18, 1, 0.2),
    (18, 2, 0.3),
    (18, 3, 0.4),
    (18, 4, 0.1),
    (19, 1, 0.3),
    (19, 2, 0.4),
    (19, 3, 0.1),
    (19, 4, 0.2),
    (20, 1, 0.4),
    (20, 2, 0.1),
    (20, 3, 0.2),
    (20, 4, 0.3),
]

mc = MarkovChain(edges)
plot_graph(mc)