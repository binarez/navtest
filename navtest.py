import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
import networkx as nx

@dataclass
class Node:
    nom: str
    position: np.ndarray  # [x, y, z]
    rotation: np.ndarray  # [rot_x, rot_y, rot_z]

nodes_gauche = [
    Node("station1",    np.array([657.37,  25.80, 58.50]), np.array([0.0,   0.0, 126.0])),
    Node("station2",    np.array([657.37, 291.20, 58.50]), np.array([0.0,   0.0, 234.0])),
    Node("processor",   np.array([455.15, 317.15, 51.25]), np.array([0.0,   0.0, 270.0])),
    Node("bargeB",      np.array([365.20, 241.64, 73.54]), np.array([0.0,  30.0,   0.0])),
    Node("bargeR",      np.array([365.20,  75.39, 73.54]), np.array([0.0,  30.0,   0.0])),
    Node("reef1",       np.array([530.49, 130.17, 12.13]), np.array([0.0,   0.0, 300.0])),
    Node("reef2",       np.array([546.87, 158.50, 12.13]), np.array([0.0,   0.0,   0.0])),
    Node("reef3",       np.array([530.49, 186.83, 12.13]), np.array([0.0,   0.0,  60.0])),
    Node("reef4",       np.array([497.77, 186.83, 12.13]), np.array([0.0,   0.0, 120.0])),
    Node("reef5",       np.array([481.39, 158.50, 12.13]), np.array([0.0,   0.0, 180.0])),
    Node("reef6",       np.array([497.77, 130.17, 12.13]), np.array([0.0,   0.0, 240.0]))
]
nodes_droite = [
    Node("station1",    np.array([ 33.51,  25.80, 58.50]), np.array([0.0,   0.0,  54.0])),
    Node("station2",    np.array([ 33.51, 291.20, 58.50]), np.array([0.0,   0.0, 306.0])),
    Node("processor",   np.array([325.68, 241.64, 73.54]), np.array([0.0,  30.0, 180.0])),
    Node("bargeB",      np.array([325.68,  75.39, 73.54]), np.array([0.0,  30.0, 180.0])),
    Node("bargeR",      np.array([235.73,  -0.15, 51.25]), np.array([0.0,   0.0,  90.0])),
    Node("reef1",       np.array([160.39, 130.17, 12.13]), np.array([0.0,   0.0, 240.0])),
    Node("reef2",       np.array([144.00, 158.50, 12.13]), np.array([0.0,   0.0, 180.0])),
    Node("reef3",       np.array([160.39, 186.83, 12.13]), np.array([0.0,   0.0, 120.0])),
    Node("reef4",       np.array([193.10, 186.83, 12.13]), np.array([0.0,   0.0,  60.0])),
    Node("reef5",       np.array([209.49, 158.50, 12.13]), np.array([0.0,   0.0,   0.0])),
    Node("reef6",       np.array([193.10, 130.17, 12.13]), np.array([0.0,   0.0, 300.0])),
]

nodes = None
if( input("(g)auche ou (d)roite? ") == "g" ):
    nodes = nodes_gauche
else:
    nodes = nodes_droite

# Je ne trouve pas les dimensions??
# field = np.array([])

G = nx.Graph()

for node in nodes:
    G.add_node(node.nom, pos=node.position)

# Dessiner le graph
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
# 5. Draw each node as a scatter point at (x, y, z)
for nom, (x, y, z) in nx.get_node_attributes(G, 'pos').items():
    ax.scatter(x, y, z, color='blue', s=40)
    # Optionally label each point with its node ID
    ax.text(x, y, z, nom, color='red', fontsize=8)

# 6. Optional: Adjust axes labels and viewpoint
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Terrain')

plt.tight_layout()
plt.show()