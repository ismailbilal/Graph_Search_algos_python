from algorithms.tree_algorithms.largeur import larguer_algo
from networkx import astar_path


algorithms = {
    "largeur": {
        "algo_func": lambda tree, source: larguer_algo(tree, source)
    },
    "astar": {
        "algo_func": lambda graph, source, goal: astar_path(graph, source, goal)
    }
}