class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        def log(*args):
            if 0:
                print(*args)
                
        n = len(scores)
        adj = collections.defaultdict(set)
        
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        top_three = collections.defaultdict(list)
        
        for u in range(n):
            for v in adj[u]:
                top_three[u].append((scores[v], v))
                
        for k in top_three:
            top_three[k].sort(reverse=True)
            top_three[k] = top_three[k][:3]
        log('top_three', top_three)
        
        res = -1
        
        def find(a, b):
            nonlocal res
            seen = set([a, b])
            
            for _, v in top_three[a]:
                if v not in seen:
                    seen.add(v)
                    break
                    
            for _, v in top_three[b]:
                if v not in seen:
                    seen.add(v)
                    break
                    
            if len(seen) == 4:
                cand = 0
                
                for v in seen:
                    cand += scores[v]
                    
                if cand > res:
                    log('a, b', a, b)
                    log('cand', cand)
                    log('seen', seen)
                    res = cand
                    
        for a, b in edges:
            find(a, b)
            find(b, a)
                
        return res
