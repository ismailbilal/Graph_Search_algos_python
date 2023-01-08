def inorder(tree, source=0, path=None):
    def iter_children(node, idx_from, idx_to):
        for child in tree[node][idx_from:idx_to]:
            if child in path: continue
            inorder(tree, child, path)

    if path is None:
        path = list()

    if tree is None:
        return
    if source not in tree:
        return
    n = len(tree[source])
    half = n // 2 + n % 2

    iter_children(source, 0, half)
    path.append(source)
    iter_children(source, half, n)

    return path
