import networkx as nx
import matplotlib.pyplot as plt
# G= nx.Graph()
# G.add_node(1)
# G.add_nodes_from([2, 3])
# G.add_nodes_from([(4, {"color": "red"}),(5, {"color": "green"}),])
# H = nx.path_graph(10)
# G.add_nodes_from(H)
# G.add_node(H)
G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()