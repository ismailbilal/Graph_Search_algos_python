def bellman_ford(M, start, goal):
    distance = []
    preview = {x: None for x in range(len(M))}
    path = [goal]
    for i in range(len(M)):
        distance.append(float('inf'))
    distance[start] = 0
    for v in range(len(M) - 1):
        for u in range(len(M)):
            for i in range(len(M)):
                if M[u, i] != 0:
                    alt = distance[u] + M[u, i]
                    if alt < distance[i] and distance[u] != float('inf'):
                        distance[i] = alt
                        preview[i] = u
    for u in range(len(M)):
        for i in range(len(M)):
            if M[u, i] != 0:
                if distance[i] > distance[u] + M[u, i]:
                    return None

    # Reconstruction du chemin a partir du preview
    u = goal
    while u != start:
        path.append(preview[u])
        u = preview[u]
    path.reverse()
    return path
