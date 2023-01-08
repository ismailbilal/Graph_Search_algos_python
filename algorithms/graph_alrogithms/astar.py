import networkx as nx
import numpy as np


def heuristic(graph, goal, ceof=1):
    return [(len(nx.astar_path(graph, source=node, target=goal)) - 1) * ceof for node in graph.nodes()]


def successors(graph, node):
    return np.where(graph[node] > 0)[1]


def in_list(lst, node):
    for ele in lst:
        if ele['node'] == node['node']:
            return True
    return False


def index_in_list(lst, node):
    for i in range(len(lst)):
        if lst[i]['node'] == node['node']:
            return i
    return None


def path(node):
    if node['parent']:
        return path(node['parent']) + [node['node']]
    return [node['node']]


def astar(graph, her, source):
    open_file = []
    closed = []
    open_file.append({
        'node': source,
        'gn': 0,
        'fn': her[source],
        'parent': None
    })
    while True:
        if not open_file:
            return []
        curr_node = min(open_file, key=lambda ele: ele['fn'])
        open_file.remove(curr_node)
        closed.append(curr_node)
        if her[curr_node['node']] == 0:
            return path(curr_node)
        for successor in successors(graph, curr_node['node']):
            gn = curr_node['gn'] + graph[curr_node['node'], successor]
            succ_node = {
                'node': successor,
                'gn': gn,
                'fn': gn + her[successor],
                'parent': curr_node
            }
            if in_list(open_file, succ_node):
                ind = index_in_list(open_file, succ_node)
                if succ_node['fn'] > open_file[ind]['fn']:
                    open_file[ind] = succ_node
            elif in_list(closed, succ_node):
                ind = index_in_list(closed, succ_node)
                if succ_node['fn'] < closed[ind]['fn']:
                    del closed[ind]
                    open_file.insert(0, succ_node)
            else:
                open_file.insert(0, succ_node)
