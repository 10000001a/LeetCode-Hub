class Trie:
    def __init__(self):
        self.x = {}

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            if word[0:i + 1] in self.x:
                if word[0:i + 1] == word:
                    self.x[word[0:i + 1]].insert(0, word)
                else:   
                    self.x[word[0:i + 1]].append(word)
            else:
                self.x[word[0:i + 1]] = [word]

    def search(self, word: str) -> bool:
        if self.x.get(word):
            return self.x.get(word)[0] == word
        return False

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.x
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)