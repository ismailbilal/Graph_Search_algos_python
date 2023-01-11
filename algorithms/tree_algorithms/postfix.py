def postfix(tree, source=0, path=None):
    if path is None:
        path = []
    if tree is None:
        return
    for child in tree[source]:
        if child in path:
            continue
        postfix(tree, child, path)
    path.append(source)
    return path
