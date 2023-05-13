import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml('karate.gml')
nx.draw_networkx(G, with_labels=True)
plt.show()
