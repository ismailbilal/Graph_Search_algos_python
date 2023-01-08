import networkx as nx
from random import choice, randint


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0., xcenter=0.5, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


def generate_tree(nb_nodes):
    G = nx.random_tree(nb_nodes, seed=randint(1, 100))
    DG = to_directed(G)
    return DG


def to_directed(tree, source=0):
    def tuple_exist_in_list(lst, tup):
        return any([sorted(tup) == sorted(ele) for ele in lst])

    def getDiEdges(tree, node, edges=[]):
        for neig in tree.neighbors(node):
            if not tuple_exist_in_list(edges, (node, neig)):
                edges.append((node, neig))
                getDiEdges(tree, neig, edges)
        return edges

    if not tree:
        return None
    if not tree.edges():
        return None
    prev_edges = tree.edges()
    DT = nx.DiGraph()
    new_edges = getDiEdges(tree, source)
    DT.add_edges_from(new_edges)
    return DT
