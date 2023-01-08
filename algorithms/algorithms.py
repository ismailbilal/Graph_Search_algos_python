from algorithms.tree_algorithms.profondeur import ParcoursProfondeur_Prefix
from algorithms.tree_algorithms.largeur import larguer_algo
from networkx import astar_path
from algorithms.tree_algorithms.prefixe import prefixe
from algorithms.tree_algorithms.infixe import inorder
from algorithms.graph_alrogithms.kraskal import get_tree_by_kruksal


algorithms = {
    "largeur": {
        "algo_func": lambda tree, source: larguer_algo(tree, source)
    },
    "profondeur": {
        "algo_func": lambda tree, source: ParcoursProfondeur_Prefix(tree, source)
    },
    "prefixe": {
        "algo_func": lambda tree, source: prefixe(tree, source)
    },
    "infixe": {
        "algo_func": lambda tree, source: inorder(tree, source)
    },
    "astar": {
        "algo_func": lambda graph, source, goal: astar_path(graph, source, goal)
    },
    "kraskal": {
        "algo_func": lambda graph : get_tree_by_kruksal(graph)
    }
}