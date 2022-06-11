class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.one_to_two = dict()
        for one, two in zip(keys, values):
            self.one_to_two[one] = two
        self.freq = collections.defaultdict(int)
        for w in dictionary:
            enc = ''
            ok = True
            for c in w:
                if c not in self.one_to_two:
                    ok = False
                    break
                enc += self.one_to_two[c]
            if ok:
                self.freq[enc] += 1

    def encrypt(self, word1: str) -> str:
        enc = ''
        for c in word1:
            enc += self.one_to_two[c]
        return enc

    def decrypt(self, word2: str) -> int:
        return self.freq[word2]
