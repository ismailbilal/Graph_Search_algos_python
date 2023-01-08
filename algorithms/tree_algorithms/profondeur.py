def ParcoursProfondeur_Prefix(Graphe, Node, listed_path_prefix=None):
    if listed_path_prefix is None:  # O(1)
        listed_path_prefix = []
    if Node not in listed_path_prefix:
        listed_path_prefix.append(Node)  # O(1)
    if Node in Graphe:  # O(1)
        Nodes_NonVisite = [n for n in Graphe[Node] if n not in listed_path_prefix]  # O👎
        for i in Nodes_NonVisite:  # O👎
            ParcoursProfondeur_Prefix(Graphe, i, listed_path_prefix)  # O(n-1)
    return listed_path_prefix
