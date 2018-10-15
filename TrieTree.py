208. Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word
        
    def startsWith(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)   


 212. Word Search II
       
这道题是在之前那道Word Search 词语搜索的基础上做了些拓展，之前是给一个单词让判断是否存在，现在是给了一堆单词，让返回所有存在的单词，
在这道题最开始更新的几个小时内，用brute force是可以通过OJ的，就是在之前那题的基础上多加一个for循环而已，
但是后来出题者其实是想考察字典树的应用，所以加了一个超大的test case，以至于brute force无法通过，强制我们必须要用字典树来求解。
那么我们在这题中只要实现字典树中的insert功能就行了，查找单词和前缀就没有必要了，然后DFS的思路跟之前那道Word Search 词语搜索基本相同     
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True
    
    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word
            
class Solution:
    def findWords(self, board, words):
        res = []
        trie = TrieTree()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, '', res)
        return res
        
    def dfs(self, board, node, i, j, path, res):
        if node.word:
            res.append(path)
            node.word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        temp = board[i][j]
        node = node.children.get(temp)
        if not node:
            return
        board[i][j] = '#'
        self.dfs(board, node, i-1, j, path+temp, res)
        self.dfs(board, node, i+1, j, path+temp, res)
        self.dfs(board, node, i, j-1, path+temp, res)
        self.dfs(board, node, i, j+1, path+temp, res)
        
        board[i][j] = temp
        
        
211. Add and Search Word - Data structure design
DFS!

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True
    def search(self, word):
        return self.dfs(self.root, word)

    def dfs(self, node, word):
        for i in range(len(word)):
            if word[i] == '.':
                for k in node.children:
                    if self.dfs(node.children[k], word[i+1:]):
                        return True
                return False
            elif word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.word
