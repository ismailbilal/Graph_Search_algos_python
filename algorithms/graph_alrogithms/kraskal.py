import networkx as nx
from tools.tree_tools import to_directed


# Classe représentant un graphe
class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    # Fonction pour ajouter une arête au graphe
    def add_edge(self, u, v, w):
        # (u, v, w) triplet représente une arête non dirigée à partir de
        self.graph.append([u, v, w])
        # sommet `u` au sommet `v` ayant le poids `w`


# Fonction pour trouver le représentant d'un sommet (utilisée dans l'algorithme de Kruskal)
# ou bien find(self, vertex):
def search(self, parent, i):
    if parent[i] == i:
        return i
    return search(self, parent, parent[i])


# Fonction pour fusionner deux ensembles (utilisée dans l'algorithme de Kruskal)


def apply_union(self, parent, rank, x, y):
    xroot = search(self, parent, x)
    yroot = search(self, parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


# fonction pour transforme une graph on forme matrix vers un objet de class Graph:


def matrixToGraph(M):
    gr = Graph(len(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != 0:
                gr.add_edge(i, j, M[i][j])
    return gr


# Fonction pour trouver l'ACPM du graphe en utilisant l'algorithme de Kruskal
# M un matrix
def kruskal(M):
    self = matrixToGraph(M)
    result = []  # Liste pour stocker l'ACPM
    i, e = 0, 0  # i Index pour parcourir les arêtes du graphe  et e Compteur d'arêtes ajoutées à l'ACPM
    # Trier les arêtes du graphe par poids croissant
    self.graph = sorted(self.graph, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(self.V):
        parent.append(node)
        rank.append(0)
    # Répéter jusqu'à ce que toutes les arêtes du graphe aient été examinées
    while e < self.V - 1:
        # Prendre l'arête suivante dans l'ordre croissant de poids
        u, v, w = self.graph[i]
        i = i + 1
        # source_set
        x = search(self, parent, u)
        # destination_set
        y = search(self, parent, v)
        # Vérifier si l'ajout de cette arête ne forme pas de cycle
        if x != y:
            e = e + 1
            # Ajouter l'arête à l'ACPM "result" et fusionner les ensembles
            result.append([u, v, w])
            apply_union(self, parent, rank, x, y)
    # Afficher l'ACPM trouvé
    for u, v, weight in result:
        # print("Edge:",u, v,end =" ")
        # print("-",weight)
        self.graph = result
        return result


def get_tree_by_kruksal(graph_as_matrix):
    edges = kruskal(graph_as_matrix)
    tree = nx.Graph()
    for u, v, w in edges:
        tree.add_edge(u, v, weight=w)
    return to_directed(tree)
