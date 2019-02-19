class WordDictionary(object):
    '''
    Design a data structure that supports the following two operations:
    void addWord(word)
    bool search(word)

    search(word) can search a literal word or a regular expression string containing only letters a-z or ".".
    A "." means it can represent any one letter.

    Example: 
    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

    https://leetcode.com/problems/add-and-search-word-data-structure-design/
    '''
    
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
