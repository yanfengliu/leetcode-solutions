# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be
# a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        global_max = 0
        current_max = 0
        index = {}
        result = ''
        for i in range(len(s)):
            if (not (s[i] in index)) or (index[s[i]][0] == 0):
                index[s[i]] = [1, i]
                current_max += 1
            else:
                current_max = i - index[s[i]][1]
                cut = index[s[i]]
                for letter, idx in index.items():
                    if idx < cut:
                        index[letter][0] = 0
                index[s[i]] = [1, i]
            global_max = max(global_max, current_max)
        return global_max
        
