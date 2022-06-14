class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        sets = collections.defaultdict(set)
        for word in ideas:
            sets[word[0]].add(word[1:])
        ans = 0
        for s1, s2 in itertools.combinations(sets.values(), 2):
            both = len(s1 & s2)
            ans += (len(s1) - both) * (len(s2) - both)
        return ans * 2
