def larguer_algo(tree, current_node):
    list_p = [current_node]
    queue = [current_node]
    while queue:
        s = queue.pop(0)
        for neighbour in tree[s]:
            if neighbour not in list_p:
                list_p.append(neighbour)
                queue.append(neighbour)
    return list_p
