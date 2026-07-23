# Last updated: 23/07/2026, 10:59:12
from collections import defaultdict

class Solution:
    def validPath(self, n, edges, source, destination):
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)