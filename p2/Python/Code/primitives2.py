import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create a sample graph
G = nx.DiGraph()

# Add nodes with uncertainty levels (0 to 1, where 1 is most certain)
nodes = [
    ('Asian', 0.9),
    ('White', 0.7),
    ('Hispanic/Latino', 0.8),
    ('African American/Black', 0.6),
    ('American Indian/Alaska Native', 0.5),
    ('Bachelors_Degree_Percent', 0.95),
    ('Unemployment', 0.85)
]

# Add edges with uncertainty levels
edges = [
    ('Asian', 'Unemployment', 0.9),
    ('White', 'Unemployment', 0.7),
    ('Hispanic/Latino', 'Unemployment', 0.8),
    ('African American/Black', 'Unemployment', 0.6),
    ('American Indian/Alaska Native', 'Unemployment', 0.5),
    ('Asian', 'Bachelors_Degree_Percent', 0.95),
    ('White', 'Bachelors_Degree_Percent', 0.85),
    ('African American/Black', 'Bachelors_Degree_Percent', 0.75)
]

# Add nodes to the graph
for node, certainty in nodes:
    G.add_node(node, certainty=certainty)

# Add edges to the graph
for src, dst, certainty in edges:
    G.add_edge(src, dst, certainty=certainty)

# Draw the graph with uncertainty visualization
pos = nx.spring_layout(G)

node_color = [G.nodes[node]['certainty'] for node in G.nodes]
node_size = [G.nodes[node]['certainty'] * 1000 for node in G.nodes]
edge_color = [G.edges[edge]['certainty'] for edge in G.edges]
edge_width = [G.edges[edge]['certainty'] * 2 for edge in G.edges]

nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size, cmap=plt.cm.Blues, alpha=0.7)
nx.draw_networkx_labels(G, pos)

# Function to draw blurred edges
def draw_blurred_edges(G, pos, edge_color, edge_width, n_blur=5):
    for edge in G.edges(data=True):
        src, dst, data = edge
        certainty = data['certainty']
        alpha = 1 - certainty
        for i in range(n_blur):
            offset = np.random.normal(0, alpha * 0.1, 2)
            nx.draw_networkx_edges(
                G, pos, edgelist=[(src, dst)],
                width=edge_width[G.edges().index(edge)] * (1 - i / n_blur),
                alpha=alpha,
                edge_color=[edge_color[G.edges().index(edge)]],
                edge_cmap=plt.cm.Purples
            )

draw_blurred_edges(G, pos, edge_color, edge_width)

plt.title("Network with Uncertainty Visualization")
plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.Blues), label='Node Certainty')
plt.show()
