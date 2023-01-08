def prefixe(tree, source=0, path=None):
    if path is None:
        path = []
    if tree is None:
        return path
    if source not in tree:
        return path
    path.append(source)
    for child in tree[source]:
        if child in path: continue
        prefixe(tree, child, path)
    return path
