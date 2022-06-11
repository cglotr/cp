class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.d = collections.defaultdict(int)
        self.m = {}
        for a, b in zip(keys, values):
            self.m[a] = b
        for w in dictionary:
            s = ''
            for c in w:
                s += self.m.get(c, '_')
            self.d[s] += 1

    def encrypt(self, word1: str) -> str:
        s = ''
        for c in word1:
            s += self.m[c]
        return s

    def decrypt(self, word2: str) -> int:
        return self.d[word2]
