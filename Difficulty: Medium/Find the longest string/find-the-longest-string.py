class Solution:
    def longestString(self, words):
        word_set = set(words)
        words.sort()
        result = ""

        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break
            if valid:
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word

        return result
