from numpy import where


def best_first_search(graph_as_matrix, source, target):
    # calculate successors of a given node
    def neighbors(node):
        return where(graph_as_matrix[node] > 0)[1]

    # generate the path from the dict parent ...
    def path(dict_parent, node_source, node):
        return (path(dict_parent, node_source, dict_parent[node]) if dict_parent[node] is not None else []) + [node]

    queue = [source]
    visited = set()
    parent = {source: None}

    while queue:
        curr_node = queue.pop()
        visited.add(curr_node)
        for neighbor_node in neighbors(curr_node):
            if neighbor_node in visited: continue
            parent[neighbor_node] = curr_node
            if neighbor_node == target: return path(parent, source, target)
            queue.insert(0, neighbor_node)
