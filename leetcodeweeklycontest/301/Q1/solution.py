class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_heap = []
        
        for cup in amount:
            if cup > 0:
                heapq.heappush(max_heap, -cup)
                
        ans = 0
        
        while len(max_heap) > 1:
            a = -heapq.heappop(max_heap) - 1
            b = -heapq.heappop(max_heap) - 1
            ans += 1
            if a > 0:
                heapq.heappush(max_heap, -a)
            if b > 0:
                heapq.heappush(max_heap, -b)
                
        while len(max_heap) > 0:
            ans += -heapq.heappop(max_heap)
            
        return ans
