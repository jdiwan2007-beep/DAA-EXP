import heapq


# Union Find Class for Kruskal's Algorithm
class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):

        root1 = self.find(x)
        root2 = self.find(y)

        if root1 == root2:
            return False

        if self.rank[root1] < self.rank[root2]:
            root1, root2 = root2, root1

        self.parent[root2] = root1

        if self.rank[root1] == self.rank[root2]:
            self.rank[root1] += 1

        return True


# Kruskal's Algorithm
def kruskal(n, edges):

    edges.sort()

    uf = UnionFind(n)

    mst = []
    total_cost = 0

    for weight, u, v in edges:

        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

        if len(mst) == n - 1:
            break

    return mst, total_cost


# Prim's Algorithm
def prim(n, graph, start=0):

    visited = [False] * n
    parent = [-1] * n
    key = [float("inf")] * n

    key[start] = 0

    pq = [(0, start)]

    mst = []
    total_cost = 0

    while pq:

        weight, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, weight))
            total_cost += weight

        for v, w in graph.get(u, []):

            if not visited[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(pq, (w, v))

    return mst, total_cost


# Main Program

n = 7

edges = [
    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)
]

graph = {}

for weight, u, v in edges:
    graph.setdefault(u, []).append((v, weight))
    graph.setdefault(v, []).append((u, weight))


kruskal_mst, kruskal_cost = kruskal(n, edges[:])
prim_mst, prim_cost = prim(n, graph)


print("Kruskal's Algorithm")
print("--------------------")

for u, v, w in kruskal_mst:
    print("Edge:", u, "-", v, " Weight =", w)

print("Total Cost =", kruskal_cost)


print("\nPrim's Algorithm")
print("--------------------")

for u, v, w in prim_mst:
    print("Edge:", u, "-", v, " Weight =", w)

print("Total Cost =", prim_cost)