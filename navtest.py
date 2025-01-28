from typing import List
import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib import animation
import networkx as nx

# Je ne trouve pas les dimensions??
TAILLE_TERRAIN = np.array([1000, 1000])

@dataclass
class Noeud:
    nom: str
    position: np.ndarray  # [x, y, z]
    rotation: np.ndarray  # [rot_x, rot_y, rot_z]

def main():
    G = nx.Graph()
    noeuds = ObtenirGraphTerrain()
    for noeud in noeuds:
        G.add_node(noeud.nom, pos=noeud.position)
    dessiner_graph(G)

def ObtenirGraphTerrain() -> List[Noeud]:
    noeuds_gauche = [
        Noeud("station1",    np.array([657.37,  25.80, 58.50]), np.array([0.0,   0.0, 126.0])),
        Noeud("station2",    np.array([657.37, 291.20, 58.50]), np.array([0.0,   0.0, 234.0])),
        Noeud("processor",   np.array([455.15, 317.15, 51.25]), np.array([0.0,   0.0, 270.0])),
        Noeud("bargeB",      np.array([365.20, 241.64, 73.54]), np.array([0.0,  30.0,   0.0])),
        Noeud("bargeR",      np.array([365.20,  75.39, 73.54]), np.array([0.0,  30.0,   0.0])),
        Noeud("reef1",       np.array([530.49, 130.17, 12.13]), np.array([0.0,   0.0, 300.0])),
        Noeud("reef2",       np.array([546.87, 158.50, 12.13]), np.array([0.0,   0.0,   0.0])),
        Noeud("reef3",       np.array([530.49, 186.83, 12.13]), np.array([0.0,   0.0,  60.0])),
        Noeud("reef4",       np.array([497.77, 186.83, 12.13]), np.array([0.0,   0.0, 120.0])),
        Noeud("reef5",       np.array([481.39, 158.50, 12.13]), np.array([0.0,   0.0, 180.0])),
        Noeud("reef6",       np.array([497.77, 130.17, 12.13]), np.array([0.0,   0.0, 240.0]))
    ]
    noeuds_droite = [
        Noeud("station1",    np.array([ 33.51,  25.80, 58.50]), np.array([0.0,   0.0,  54.0])),
        Noeud("station2",    np.array([ 33.51, 291.20, 58.50]), np.array([0.0,   0.0, 306.0])),
        Noeud("processor",   np.array([325.68, 241.64, 73.54]), np.array([0.0,  30.0, 180.0])),
        Noeud("bargeB",      np.array([325.68,  75.39, 73.54]), np.array([0.0,  30.0, 180.0])),
        Noeud("bargeR",      np.array([235.73,  -0.15, 51.25]), np.array([0.0,   0.0,  90.0])),
        Noeud("reef1",       np.array([160.39, 130.17, 12.13]), np.array([0.0,   0.0, 240.0])),
        Noeud("reef2",       np.array([144.00, 158.50, 12.13]), np.array([0.0,   0.0, 180.0])),
        Noeud("reef3",       np.array([160.39, 186.83, 12.13]), np.array([0.0,   0.0, 120.0])),
        Noeud("reef4",       np.array([193.10, 186.83, 12.13]), np.array([0.0,   0.0,  60.0])),
        Noeud("reef5",       np.array([209.49, 158.50, 12.13]), np.array([0.0,   0.0,   0.0])),
        Noeud("reef6",       np.array([193.10, 130.17, 12.13]), np.array([0.0,   0.0, 300.0])),
    ]
    while True:
        choix = input("Champ de (g)auche ou (d)roite? ")
        if( choix == "g" ):
            return noeuds_gauche
        elif( choix == "d" ):
            return noeuds_droite

def dessiner_graph(G : nx.Graph):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    for nom, (x, y, z) in nx.get_node_attributes(G, 'pos').items():
        ax.scatter(x, y, z, color='blue', s=40)
        ax.text(x, y, z, nom, color='red', fontsize=8)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Terrain')
    plt.tight_layout()
    plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection="3d")
# ax.grid(False)
# ax.set_axis_off()
# plt.tight_layout()
# noeud = [0]
# ani = animation.FuncAnimation(
#     fig,
#     mise_a_jour_anim,
#     interval=50,
#     cache_frame_data=False,
#     frames=100,
# )
# # plt.show()
# def mise_a_jour_anim(index):
#     ax.clear()
#     ax.scatter(*noeuds.T, alpha=0.2, s=100, color="blue")
#     for vizedge in edges:
#         ax.plot(*vizedge.T, color="gray")
#     neighbors = list(G.neighbors(noeud[0]))
#     if index % 5 == 0:
#         noeud[0] = random.choice(neighbors)
#     noeud0 = noeuds[noeud[0]]
#     ax.scatter(*noeud0, alpha=1, marker="s", color="red", s=100)
#     ax.view_init(index * 0.2, index * 0.5)
#     ax.grid(False)
#     # ax.set_axis_off()
#     plt.tight_layout()
#     return

# C'est parti!
main()
