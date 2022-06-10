class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = collections.defaultdict(int)
        players = set()
        
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loses[loser] += 1
            
        ans = [[],[]]
        
        for player in players:
            if loses[player] == 0:
                ans[0].append(player)
            elif loses[player] == 1:
                ans[1].append(player)
                
        ans[0].sort()
        ans[1].sort()
                
        return ans
