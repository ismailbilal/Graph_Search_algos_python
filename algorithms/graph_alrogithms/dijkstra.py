import sys
import numpy as np


def successors(graph, node):
    return np.where(graph[node] > 0)[1]


def min_dist_not_closed(dist, closed):
    return dist.index(min([dist[i] for i in range(len(dist)) if not closed[i]]))


def dijkstra(graph, start, goal):
    dist = [sys.maxsize for i in range(len(graph))]
    path = [[] for i in range(len(graph))]
    dist[start] = 0
    path[start] = [start]
    closed = [False for i in range(len(graph))]
    while not all(closed):
        curr_node = min_dist_not_closed(dist, closed)
        closed[curr_node] = True
        for nd in successors(graph, curr_node):
            F = dist[curr_node] + graph[curr_node, nd]
            if dist[nd] > F:
                dist[nd] = F
                path[nd] = path[curr_node] + [nd]
    return path[goal]
