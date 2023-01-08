from algorithms.tree_algorithms.profondeur import ParcoursProfondeur_Prefix
from algorithms.tree_algorithms.largeur import larguer_algo
from networkx import astar_path


algorithms = {
    "largeur": {
        "algo_func": lambda tree, source: larguer_algo(tree, source)
    },
    "profondeur": {
        "algo_func": lambda tree, source: ParcoursProfondeur_Prefix(tree, source)
    },
    "astar": {
        "algo_func": lambda graph, source, goal: astar_path(graph, source, goal)
    }
}