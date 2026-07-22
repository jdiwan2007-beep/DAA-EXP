import heapq


# Dijkstra's Algorithm
def dijkstra(graph, source):

    n = len(graph)

    distance = [float("inf")] * n
    parent = [None] * n

    distance[source] = 0

    pq = [(0, source)]
    visited = [False] * n

    while pq:

        dist, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        for v, weight in graph[u]:

            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u

                heapq.heappush(pq, (distance[v], v))

    return distance, parent


# Function to print shortest path
def get_path(parent, source, vertex):

    path = []

    while vertex is not None:
        path.append(vertex)
        vertex = parent[vertex]

    path.reverse()

    if path[0] == source:
        return path

    return []


# Main Program

graph = {
    0: [(1, 2), (2, 6)],
    1: [(2, 3), (3, 1)],
    2: [(3, 2), (4, 5)],
    3: [(4, 1), (5, 4)],
    4: [(5, 2)],
    5: []
}

source = 0

distance, parent = dijkstra(graph, source)

print("Source Vertex =", source)
print()

print("Vertex\tDistance\tPath")
print("-----------------------------------------")

for i in range(len(graph)):

    path = get_path(parent, source, i)

    if distance[i] == float("inf"):
        d = "INF"
    else:
        d = distance[i]

    print(i, "\t", d, "\t\t", " -> ".join(map(str, path)))