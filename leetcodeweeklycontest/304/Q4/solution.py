class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        WHITE = 0
        GRAY = 1
        BLACK = 2
        
        n = len(edges)
        graph = collections.defaultdict(int)
        sources = set([i for i in range(n)])
        
        for u in range(n):
            v = edges[u]
            if v != -1:
                graph[u] = v
            sources.discard(v)
                
        colors = [WHITE for _ in range(n)]
        dist = [math.inf for _ in range(n)]
        
        ans = -1
        
        def dfs(u, depth):
            nonlocal ans
            
            colors[u] = GRAY
            dist[u] = depth
            
            if u in graph:
                v = graph[u]

                if colors[v] == GRAY:
                    d = depth - dist[v] + 1
                    ans = max(ans, d)
                elif colors[v] == WHITE:
                    dfs(v, depth + 1)
                
            colors[u] = BLACK
            
        for u in range(n):
            dfs(u, 0)
                
        return ans
