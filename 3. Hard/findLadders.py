class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        if not (beginWord in wordList):
            wordList += [beginWord]
        if not (endWord in wordList):
            return []
        else:
            adjList = self.build_adjacency_list(wordList)
            adjList[beginWord][1] = 0
            adjList[beginWord][3] = 1
            adjList = self.BFS(adjList, beginWord)
            wordGraph = self.build_word_graph(adjList)
            paths = self.get_path(wordGraph, endWord)
            if(adjList[endWord][1] == float("inf")):
                return []
            else:
                ans = []
                for key in paths:
                    ans.append(paths[key])
                return ans
    
    def build_adjacency_list(self, wordList):
        adjList = {}
        wordList = set(wordList)
        for a in wordList:
            adjList[a] = [[], float("inf"), [], 0] 
            for i in range(len(a)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    b = a[:i] + j + a[(i+1):]
                    if b in wordList:
                        adjList[a][0] += [b]
        return adjList
    
    def BFS(self, adjList, s):
        import collections 
        Q = collections.deque()
        Q.append(s)
        while Q:
            u = Q.popleft()
            for v in adjList[u][0]:
                if adjList[v][3] == 0:
                    adjList[v][3] = 1
                    adjList[v][1] = adjList[u][1] + 1
                    adjList[v][2] = [u]
                    Q.append(v)
                else:
                    if adjList[v][1] == adjList[u][1] + 1:
                        if not (u in adjList[v][2]):
                            adjList[v][2] += [u]
        return adjList
    
    def get_path(self, wordGraph, wordName):
        node = wordGraph[wordName]
        if (node.predecessors != []):
            paths = {}
            predecessors = node.predecessors
            idx = 1
            for p in predecessors:
                previousPaths = self.get_path(wordGraph, p)
                for key in previousPaths:
                    paths[idx] = previousPaths[key] + [wordName]
                    idx += 1
            node.paths = paths
            return paths
        else:
            return {1: [wordName]}
    
    def build_word_graph(self, adjList):
        wordGraph = {}
        for word in adjList:
            if not (word in wordGraph):
                wordGraph[word] = Node(word, adjList[word][2], {})
        return wordGraph
        
class Node(object):
    word = ""
    predecessors = []
    paths = {}

    def __init__(self, word, predecessors, paths):
        self.word = word
        self.predecessors = predecessors
        self.paths = paths
    
    
