# Given a string, you need to reverse the order of characters in each word within a sentence while 
# still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        reverse_words = []
        for word in words:
            reverse_words.append(word[::-1])
        reverse_sentence = ' '.join(reverse_words)
        return reverse_sentence
