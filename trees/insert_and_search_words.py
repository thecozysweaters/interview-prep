class WordDictionary(object):
    def __init__(self):
        self.children = {}
    
    def addWord(self, word):
        letters = list(word)
        if len(letters) == 0: return

        c = letters.pop(0)
        if c not in self.children: 
            self.children[c] = WordDictionary()
        self.children[c].addWord(letters)
    
    def findWord(self, word):
        letters = list(word)
        print(letters)
        if len(letters) == 0: return True
        
        c = letters.pop(0)
        if c == ".":
            for letter in self.children:
                return self.children[letter].findWord(letters)
        elif c not in self.children: return False
        else: return self.children[c].findWord(letters)
