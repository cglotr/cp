class TextEditor:

    def __init__(self):
        self.text = ''
        self.cursor = 0

    def addText(self, text: str) -> None:
        l = self.text[:self.cursor]
        r = self.text[self.cursor:]
        self.text = l + text + r
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        l = self.text[:self.cursor]
        r = self.text[self.cursor:]
        d_len = min(k, len(l))
        l = l[:len(l) - d_len]
        self.text = l + r
        self.cursor -= d_len
        return d_len

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        return self.text[max(0, self.cursor - 10):self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.text), self.cursor + k)
        return self.text[max(0, self.cursor - 10):self.cursor]
