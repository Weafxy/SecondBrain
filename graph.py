import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(notes):
    G = nx.Graph()
    for note in notes:
        G.add_node(note["id"], label=note["title"])
        for link_id in note["links"]:
            G.add_edge(note["id"], link_id)

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color="skyblue", font_size=10)
    plt.show()