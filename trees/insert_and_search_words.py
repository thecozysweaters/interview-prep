class WordDictionary(object):
  def __init__(self, letter=None):
    self.letter = letter
    self.children = {}
  
  def addWord(self, word):
    for i in range(len(word)):
      c = word[i]
      if c not in self.children:
        self.children[c] = WordDictionary(c)
      self.addWord(self.children[c], word[i+1:])

  def searchWord(self, word):
    # base case: we've traversed through everything and found all the letters
    if word == "": return True

    # otherwise, let's traverse through the letters of the word
    for i in range(len(word)):
      c = word[i]
      # if c is a wildcard, we must consider all possible paths
      if c == ".":
        for nextLetter in self.children:
          return self.searchWord(self.children[nextLetter], word[i+1:])
      # if c is not a wildcard and not in the children, it's False
      elif c not in self.children: 
        return False
      # if c is in the children, continue traversing
      else:
        return self.searchWord(self.children[c], word[i+1:])