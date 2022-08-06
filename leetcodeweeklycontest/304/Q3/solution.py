class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = collections.defaultdict(list)
        
        for u in range(n):
            v = edges[u]
            if v != -1:
                graph[u].append(v)
                
        def dfs(u, depth, dist):
            dist[u] = depth
            
            for v in graph[u]:
                if v not in dist:
                    dfs(v, depth + 1, dist)
                    
        dist1 = collections.defaultdict(lambda: math.inf)
        dist2 = collections.defaultdict(lambda: math.inf)
                    
        dfs(node1, 0, dist1)
        dfs(node2, 0, dist2)
        
        ans = -1
        ans_dist = math.inf
        
        for u in range(n):
            v = max(dist1[u], dist2[u])
            if v < ans_dist:
                ans = u
                ans_dist = v
        
        return ans
