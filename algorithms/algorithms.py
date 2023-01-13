from algorithms.tree_algorithms.profondeur import ParcoursProfondeur_Prefix
from algorithms.tree_algorithms.largeur import larguer_algo
from algorithms.tree_algorithms.prefixe import prefixe
from algorithms.tree_algorithms.infixe import inorder
from algorithms.graph_alrogithms.kraskal import get_tree_by_kruksal
from algorithms.graph_alrogithms.astar import astar, heuristic
from algorithms.graph_alrogithms.dijkstra import dijkstra
from algorithms.tree_algorithms.postfix import postfix
from networkx import from_numpy_matrix

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
    "postfixe": {
        "algo_func": lambda tree, source: postfix(tree, source)
    },
    "astar": {
        "algo_func": lambda graph, source, goal: astar(graph, heuristic(from_numpy_matrix(graph), goal), source)
    },
    "dijkstra": {
        "algo_func": lambda graph, source, goal: dijkstra(graph, source, goal)
    },
    "kraskal": {
        "algo_func": lambda graph: get_tree_by_kruksal(graph)
    }
}
