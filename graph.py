"""
Assessment 3.3 - Non-Linear Data Structure
Program 2: Graph using the last name FUENTES  (BFS and DFS traversal)

The vertices are the letters of FUENTES. Because the letter E appears twice,
each vertex is identified by its position in the name (0 to 6) and shown
using its letter:

    position: 0  1  2  3  4  5  6
    letter:   F  U  E  N  T  E  S

Edges (by letter): F-U, F-E(pos 2), F-T, U-N, U-E(pos 5), E(pos 2)-T,
                   E(pos 2)-E(pos 5), N-S, T-S
Levels from F: level 0 = F | level 1 = U, T, E(pos 2) | level 2 = N, E(pos 5), S
"""
from collections import deque

NAME = "FUENTES"

# Adjacency list: each vertex (position) -> list of connected vertices.
# The order of neighbors decides the order of visiting.
graph = {
    0: [1, 4, 2],   # F  -> U, T, E
    1: [0, 3, 5],   # U  -> F, N, E
    2: [0, 4, 5],   # E  -> F, T, E
    3: [1, 6],      # N  -> U, S
    4: [0, 2, 6],   # T  -> F, E, S
    5: [1, 2],      # E  -> U, E
    6: [3, 4],      # S  -> N, T
}


def bfs(graph, start):
    """Breadth-First Search: visit all neighbors first, then the next level (queue)."""
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:     # skip vertices already seen
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph, vertex, visited=None, order=None):
    """Depth-First Search: follow one path as far as possible, then backtrack."""
    if visited is None:
        visited, order = set(), []
    visited.add(vertex)
    order.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order


def show(order):
    """Turn positions into letters, e.g. [0, 1] -> 'F - U'."""
    return " - ".join(NAME[v] for v in order)


if __name__ == "__main__":
    print("BFS:", show(bfs(graph, 0)))
    print("DFS:", show(dfs(graph, 0)))