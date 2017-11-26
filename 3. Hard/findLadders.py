# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation 
#   sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]

# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# https://leetcode.com/problems/word-ladder-ii/description/

# ============================================================================================
# Main idea: 
#     1. Build a graph from the wordList, represented in adjacency list format.
#     2. Run Breadth-First-Search (BFS) on the graph to compute the distance of each node from beginWord.
#     3. Backtrace all paths leading to endWord based on BFS-processed graph.

# Tricks:
#     1. Writing the code that works is not the most challenging part. Making it run within
#         the time limit is.
#     2. Some people use two-end BFS to further improve the running time, but it turns out
#         building the adjacency list was the most time consuming part.
#     3. This is technically a single source shortest path problem, and generally needs a more 
#         thorough algorithm like Bellman-Ford or Dijkstra's. But for this specific problem, 
#         the distance between two nodes will always be the same if they are connected by an edge,
#         thus simplifying the problem into a BFS one. The difference in running time is huge:
#         BFS takes O(V+E), Bellman-Ford takes O(V*E), and Dijkstra's takes O(V*lg(V)+E).

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
            # Build adjacency list representation of the graph
            adjList = self.build_adjacency_list(wordList)
            # set distance on source node to 0
            adjList[beginWord][1] = 0
            # set color on source node to gray (0 is white, 1 is gray)
            adjList[beginWord][3] = 1
            # run Breadth-First Search on the graph
            adjList = self.BFS(adjList, beginWord)
            # build object oriented graph for easier path backtracing
            wordGraph = self.build_word_graph(adjList)
            # backtrace all shortest paths
            paths = self.get_path(wordGraph, endWord)
            # if endWord is unreachable from beginWord, then return empty list
            if(adjList[endWord][1] == float("inf")):
                return []
            else:
                ans = []
                for key in paths:
                    ans.append(paths[key])
                return ans
    
    def build_adjacency_list(self, wordList):
        adjList = {}
        # convert list to set for faster lookup
        wordList = set(wordList)
        for word in wordList:
            # for every word, we have the following information:
            # adjacent words, distance from beginWord, predecessors, and color.
            # distances are all initialized as infinite, and color is either 0 (white) or 1 (gray).
            adjList[word] = [[], float("inf"), [], 0]
            for i in range(len(word)):
                # don't try to compare every word with every other words in the list. 
                # it takes way too long (n^2 comparisons where n = len(wordList))
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    # there are three main ways to change a string in python
                    # but they have different speeds. use the fastest. 
                    # https://stackoverflow.com/questions/1228299/change-one-character-in-a-string
                    changed = word[:i] + j + word[(i+1):]
                    if changed in wordList:
                        adjList[word][0] += [changed]
        return adjList
    
    def BFS(self, adjList, s):
        # classic breadth first algorithm
        import collections 
        # Q is a queue of nodes to search next
        Q = collections.deque()
        # we begin at the source node
        Q.append(s)
        # while queue is not empty
        while Q:
            # get next in queue
            u = Q.popleft()
            # for every node v adjacent to the current node u
            for v in adjList[u][0]:
                # if v's color is white
                if adjList[v][3] == 0:
                    # set v's color to gray
                    adjList[v][3] = 1
                    # change v's distance to 1 + u's distance
                    adjList[v][1] = adjList[u][1] + 1
                    # change v's predecessor to u
                    adjList[v][2] = [u]
                    # add v to search queue
                    Q.append(v)
                # otherwise (if v's color is gray)
                else:
                    # if v's distance equals 1 + u's distance
                    if adjList[v][1] == adjList[u][1] + 1:
                        # if u is not already one of v's predecessors
                        if not (u in adjList[v][2]):
                            # add u to v's predecessors list
                            adjList[v][2] += [u]
        return adjList
    
    def get_path(self, wordGraph, wordName):
        node = wordGraph[wordName]
        # if node has a predecessor
        if (node.predecessors != []):
            paths = {}
            # get all of node's predecessor
            predecessors = node.predecessors
            idx = 1
            for p in predecessors:
                # recursively get path leading to the predecessor
                previousPaths = self.get_path(wordGraph, p)
                # for every path leading to the predecessor
                for key in previousPaths:
                    # append current node to the path
                    paths[idx] = previousPaths[key] + [wordName]
                    idx += 1
            node.paths = paths
            return paths
        # if node does not have a predecessor
        else:
            # then it is the beginWord. return itself. 
            return {1: [wordName]}
    
    def build_word_graph(self, adjList):
        wordGraph = {}
        for word in adjList:
            if not (word in wordGraph):
                # a node object has the following attributes:
                # its word: str, predecessors: list[str], paths: list[list[str]]
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
    
    
