import re
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        output = []
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        rows = [row1, row2, row3]
        
        for word in words:
            flag = [1, 1, 1]
            idx = 0
            for row in rows:
                for char in word.lower():
                    if char not in row:
                        flag[idx] = 0
                idx += 1
            
            if any(flag):
                output.append(word)
        return output
                
            
        
