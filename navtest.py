from typing import List
import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib import animation
import networkx as nx

# TODO Je ne trouve pas les vraies dimensions??
TAILLE_TERRAIN = np.array([1000, 350, 100])

@dataclass
class Noeud:
    nom: str
    position: np.ndarray  # [x, y, z]
    rotation: np.ndarray  # [rot_x, rot_y, rot_z]

@dataclass
class Arete:
    de: str
    vers: str

def main():
    # Obtenir les noeuds du terrain
    noeuds = ObtenirGraphTerrain()

    # Créer un graphique NetworkX
    G = nx.Graph()
    for noeud in noeuds:
        G.add_node(noeud.nom, pos=noeud.position)

    # Ajouter les arêtes
    aretes = [
        # Des stations vers les transits
        Arete("station1", "transitS"),
        Arete("station1", "transitE"),
        Arete("station2", "transitN"),
        Arete("station2", "transitE"),
        # Des transits vers les autres transits
        Arete("transitN", "transitE"),
        Arete("transitN", "transitW"),
        Arete("transitS", "transitE"),
        Arete("transitS", "transitW"),
        # Des transits vers les récifs
        Arete("transitS", "reef1"),
        Arete("transitS", "reef6"),
        Arete("transitN", "reef3"),
        Arete("transitN", "reef4"),
        Arete("transitE", "reef2"),
        Arete("transitW", "reef5"),
        # Vers le processeur
        Arete("transitN", "processor")
            ]
    noeudsGraph = nx.get_node_attributes(G, 'pos')
    for arete in aretes:
        G.add_edge(arete.de, arete.vers, weight=np.linalg.norm(noeudsGraph[arete.de] - noeudsGraph[arete.vers]))

    # Générer des chemins de démonstration
    demoChemins =   [
        nx.dijkstra_path(G, "station1", "station2"),
        nx.dijkstra_path(G, "station1", "processor"),
        nx.dijkstra_path(G, "station2", "reef6")
                    ]
    
    # Afficher!
    dessiner_graph(G, demoChemins)

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
        Noeud("reef6",       np.array([497.77, 130.17, 12.13]), np.array([0.0,   0.0, 240.0])),
        Noeud("transitN",    np.array([515, 225, 1]),  np.array([0,0,0])),
        Noeud("transitS",    np.array([515, 75, 1]),  np.array([0,0,0])),
        Noeud("transitE",    np.array([625, 158, 1]),  np.array([0,0,0])),
        Noeud("transitW",    np.array([425, 158, 1]),  np.array([0,0,0])),
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
        choix = "g"  # Debug
        # choix = input("Champ de (g)auche ou (d)roite? ")
        if( choix == "g" ):
            return noeuds_gauche
        elif( choix == "d" ):
            return noeuds_droite

def dessiner_graph(G : nx.Graph, chemins : List[str] = []):
    fig = plt.figure(figsize=(12,10))
    render = fig.add_subplot(111, projection="3d")

    def mise_a_jour_anim(frameIndex : int):
        # Réinitialiser le graphique
        render.clear()
        render.grid(True)
        render.set_xlabel('X')
        render.set_ylabel('Y')
        render.set_zlabel('Z')
        render.set_xlim([0, TAILLE_TERRAIN[0]])
        render.set_ylim([0, TAILLE_TERRAIN[1]])
        render.set_zlim([0, TAILLE_TERRAIN[2]])
        render.set_title('Terrain')
        render.set_box_aspect(TAILLE_TERRAIN)

        # Dessiner les noeuds
        noeuds = nx.get_node_attributes(G, 'pos')
        for nom, (x, y, z) in noeuds.items():
            render.scatter(x, y, z, color='blue', s=40)
            render.text(x, y, z, nom, color='red', fontsize=8)

        # Dessiner les arêtes
        for depart, arrivee in G.edges:
            noeudDepart = noeuds[depart]
            noeudArrivee = noeuds[arrivee]
            x_coords = [noeudDepart[0], noeudArrivee[0]]
            y_coords = [noeudDepart[1], noeudArrivee[1]]
            z_coords = [noeudDepart[2], noeudArrivee[2]]
            render.plot(x_coords, y_coords, z_coords, color="green", linewidth=1, alpha=0.6)

        # Dessiner les chemins
        for chemin in chemins:
            # Pour chacune des aretes du chemin
            for i in range(len(chemin)-1):
                noeudDepart = noeuds[chemin[i]]
                noeudArrivee = noeuds[chemin[i + 1]]
                x_coords = [noeudDepart[0], noeudArrivee[0]]
                y_coords = [noeudDepart[1], noeudArrivee[1]]
                z_coords = [noeudDepart[2], noeudArrivee[2]]
                render.plot(x_coords, y_coords, z_coords, color="red", linewidth=2)

        # Terminé!
        return render

    # Plotlib animation
    anim = animation.FuncAnimation(
        fig,
        mise_a_jour_anim,
        interval=50,
        cache_frame_data=False,
        frames=100)
    
    # Affichage
    plt.show()

# C'est parti!
main()
