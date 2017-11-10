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
