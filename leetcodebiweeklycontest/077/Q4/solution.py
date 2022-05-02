class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        def log(*args):
            if 0:
                print(*args)
                
        GRASS = 0
        FIRE = 1
        WALL = 2
        R = len(grid)
        C = len(grid[0])
        
        F = [[math.inf for _ in range(C)] for _ in range(R)]
        f_q = collections.deque()
        f_s = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == FIRE:
                    f_q.append((r, c, 0))
                    
        while len(f_q) > 0:
            r, c, t = f_q.popleft()
            F[r][c] = t
            f_s.add((r, c))
            
            for r_d, c_d in directions:
                r_n = r + r_d
                c_n = c + c_d
                if r_n < 0 or r_n >= R or c_n < 0 or c_n >= C:
                    continue
                if (r_n, c_n) in f_s:
                    continue
                if grid[r_n][c_n] == GRASS:
                    f_q.append((r_n, c_n, t + 1))
                    
        log('F')
        for row in F:
            log(row)
                    
        def possible(wait):
            q = collections.deque()
            q.append((0, 0, wait))
            s = set()
            
            while len(q) > 0:
                r, c, t = q.popleft()
                s.add((r, c))
                if r == R - 1 and c == C - 1 and t <= F[r][c]:
                    return True
                if t >= F[r][c]:
                    continue
                
                for r_d, c_d in directions:
                    r_n = r + r_d
                    c_n = c + c_d
                    if r_n < 0 or r_n >= R or c_n < 0 or c_n >= C:
                        continue
                    if (r_n, c_n) in s:
                        continue
                    if grid[r_n][c_n] == WALL:
                        continue
                    q.append((r_n, c_n, t + 1))
                    
            return False
        
        l = 0
        r = 2 * 10 ** 4
        
        if not possible(l):
            return -1
        
        if possible(r):
            return 10 ** 9
        
        while l < r:
            mid = (r - l + 1) // 2 + l
            if possible(mid):
                l = mid
            else:
                r = mid - 1
                
        return l
