import numpy as np


def bellman_ford_moore(M, start, goal):
    distance = np.full(M.shape[0], float('inf'))
    preview = {x: None for x in range(len(M))}
    # goal=len(M)-1  #On prendra par exemple le goal comme la fin du graphe
    path = [goal]
    distance[start] = 0
    changed = True
    iteration = 0
    while changed:
        changed = False
        # Pour chaque sommet du graphe
        for u in range(len(M)):
            # Pour chaque voisin de u
            for i in range(len(M)):
                # si on peut relacher un arc entre u et v, fait le si possible
                if M[u, i] != 0:
                    alt = distance[u] + M[u, i]
                    if alt < distance[i]:
                        distance[i] = alt
                        preview[i] = u
                        changed = True
        iteration += 1
        # s'il se met a boucler plus que la taille de la matrice il' ya la presence d'un cycle on sort directement
        if iteration > len(M) + 1:
            break
            # Detection cycle de poids negatif et si on peut encore ameliorer des distances
    for u in range(len(M)):
        for i in range(len(M)):
            if M[u, i] != 0:
                if distance[i] > distance[u] + M[u, i]:
                    return None

    # Cette dernière partie est consacré pour retrouver  le chemin
    # à partir du tableau de preédecesseur
    u = goal
    try:
        while u != start:
            path.append(preview[u])
            u = preview[u]
        path.reverse()
    except KeyError:
        print("Aucun chemin ")
    return path
